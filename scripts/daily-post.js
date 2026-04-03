#!/usr/bin/env node
/**
 * Sovren Software — Daily Content Queue Poster
 *
 * Reads content-queue.json, posts the next pending item scheduled for today or earlier.
 * Marks it as posted with timestamp and tweet ID.
 *
 * Usage:
 *   node scripts/daily-post.js              # Post next scheduled item
 *   node scripts/daily-post.js --dry-run    # Preview without posting
 *   node scripts/daily-post.js --list       # Show queue status
 *   node scripts/daily-post.js --add "text" # Add a new post to the queue
 *
 * Environment (via direnv):
 *   X_API_KEY, X_API_SECRET — app credentials (registered under @TheCesarCross)
 *   X_SOVREN_ACCESS_TOKEN, X_SOVREN_ACCESS_SECRET — posts as @sovren_software
 */

import { readFileSync, writeFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { parseArgs } from 'util';
import { TwitterApi } from 'twitter-api-v2';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const QUEUE_PATH = join(__dirname, 'content-queue.json');

function loadQueue() {
  return JSON.parse(readFileSync(QUEUE_PATH, 'utf-8'));
}

function saveQueue(queue) {
  writeFileSync(QUEUE_PATH, JSON.stringify(queue, null, 2) + '\n');
}

function today() {
  return new Date().toISOString().split('T')[0];
}

function validateVoice(text) {
  const warnings = [];
  const emojiRegex = /[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{1F1E0}-\u{1F1FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/u;

  if (emojiRegex.test(text)) warnings.push('Contains emojis');
  if (text.includes('!')) warnings.push('Contains exclamation mark');
  if (text.length > 280) warnings.push(`Over 280 chars (${text.length})`);

  const hypeWords = ['excited', 'amazing', 'incredible', 'revolutionary', 'game-changing', 'LFG', 'wagmi'];
  for (const word of hypeWords) {
    if (text.toLowerCase().includes(word.toLowerCase())) {
      warnings.push(`Contains hype word: "${word}"`);
    }
  }

  return warnings;
}

async function postToX(text) {
  const appKey = process.env.X_API_KEY;
  const appSecret = process.env.X_API_SECRET;
  const accessToken = process.env.X_SOVREN_ACCESS_TOKEN;
  const accessSecret = process.env.X_SOVREN_ACCESS_SECRET;

  if (!appKey || !appSecret || !accessToken || !accessSecret) {
    throw new Error('Missing X API credentials. Required: X_API_KEY, X_API_SECRET, X_SOVREN_ACCESS_TOKEN, X_SOVREN_ACCESS_SECRET');
  }

  const client = new TwitterApi({
    appKey,
    appSecret,
    accessToken,
    accessSecret,
  });

  const response = await client.v2.tweet(text);
  return {
    id: response.data.id,
    url: `https://x.com/sovren_software/status/${response.data.id}`,
  };
}

function listQueue(queue) {
  const now = today();
  console.log(`\n  @sovren_software content queue\n`);
  console.log(`  ${'ID'.padEnd(4)} ${'Scheduled'.padEnd(12)} ${'Status'.padEnd(10)} ${'Category'.padEnd(10)} Text`);
  console.log(`  ${'—'.repeat(80)}`);

  for (const post of queue.posts) {
    const overdue = post.status === 'pending' && post.scheduled <= now ? ' (due)' : '';
    const statusDisplay = post.status === 'posted'
      ? `posted`
      : `${post.status}${overdue}`;
    const textPreview = post.text.replace(/\n/g, ' ').slice(0, 50);
    console.log(`  ${String(post.id).padEnd(4)} ${(post.scheduled || '—').padEnd(12)} ${statusDisplay.padEnd(16)} ${(post.category || '—').padEnd(10)} ${textPreview}...`);
  }

  const pending = queue.posts.filter(p => p.status === 'pending').length;
  const posted = queue.posts.filter(p => p.status === 'posted').length;
  console.log(`\n  ${posted} posted, ${pending} pending\n`);
}

function addPost(queue, text, category) {
  const maxId = Math.max(0, ...queue.posts.map(p => p.id));
  const lastScheduled = queue.posts
    .filter(p => p.scheduled)
    .map(p => p.scheduled)
    .sort()
    .pop();

  const nextDate = lastScheduled
    ? new Date(new Date(lastScheduled).getTime() + 86400000).toISOString().split('T')[0]
    : today();

  const newPost = {
    id: maxId + 1,
    text,
    category: category || 'thesis',
    status: 'pending',
    scheduled: nextDate,
    posted_at: null,
    tweet_id: null,
  };

  queue.posts.push(newPost);
  saveQueue(queue);
  console.log(`\n  Added post #${newPost.id} scheduled for ${nextDate}\n`);
}

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      'dry-run': { type: 'boolean', short: 'd', default: false },
      list: { type: 'boolean', short: 'l', default: false },
      add: { type: 'string', short: 'a' },
      category: { type: 'string', short: 'c', default: 'thesis' },
      help: { type: 'boolean', short: 'h', default: false },
    },
    allowPositionals: true,
  });

  if (values.help) {
    console.log(`
  Sovren Software — Daily Content Queue

  Usage:
    node scripts/daily-post.js              Post next scheduled item
    node scripts/daily-post.js --dry-run    Preview without posting
    node scripts/daily-post.js --list       Show queue status
    node scripts/daily-post.js --add "text" Add a post to the queue
    node scripts/daily-post.js --add "text" --category vision
    `);
    return;
  }

  const queue = loadQueue();

  if (values.list) {
    listQueue(queue);
    return;
  }

  if (values.add) {
    addPost(queue, values.add, values.category);
    return;
  }

  // Find next post: pending + scheduled for today or earlier
  const now = today();
  const next = queue.posts.find(p => p.status === 'pending' && p.scheduled <= now);

  if (!next) {
    const nextPending = queue.posts.find(p => p.status === 'pending');
    if (nextPending) {
      console.log(`\n  No posts due today. Next scheduled: #${nextPending.id} on ${nextPending.scheduled}\n`);
    } else {
      console.log('\n  Queue empty. Add posts with --add "text"\n');
    }
    return;
  }

  // Voice check
  const warnings = validateVoice(next.text);
  if (warnings.length > 0) {
    console.log('\n  Voice warnings:');
    for (const w of warnings) console.log(`    - ${w}`);
    console.log('');
  }

  console.log(`\n  Post #${next.id} (${next.category})`);
  console.log(`  Scheduled: ${next.scheduled}`);
  console.log(`  ─────────────────────────────────`);
  console.log(`  ${next.text}`);
  console.log(`  ─────────────────────────────────`);
  console.log(`  ${next.text.length}/280 chars\n`);

  if (values['dry-run']) {
    console.log('  [dry-run] Would post the above. Run without --dry-run to post.\n');
    return;
  }

  try {
    const result = await postToX(next.text);
    next.status = 'posted';
    next.posted_at = new Date().toISOString();
    next.tweet_id = result.id;
    saveQueue(queue);
    console.log(`  Posted: ${result.url}\n`);
  } catch (err) {
    console.error(`  Failed to post: ${err.message}\n`);
    process.exit(1);
  }
}

main();
