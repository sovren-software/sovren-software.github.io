import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';
import { readFileSync, writeFileSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = resolve(__dirname, '..');

const fontRegular = readFileSync(resolve(root, 'node_modules/geist/dist/fonts/geist-mono/GeistMono-Regular.ttf'));
const fontBold = readFileSync(resolve(root, 'node_modules/geist/dist/fonts/geist-mono/GeistMono-Medium.ttf'));

// Schematic Magitek palette
const bone = '#F0EDE8';
const boneAlt = '#E8E4DF';
const charcoal = '#1A1A1A';
const violet = '#8B7EC8';
const borderLight = 'rgba(0,0,0,0.12)';
const borderStrong = 'rgba(0,0,0,0.25)';
const textMuted = 'rgba(26,26,26,0.35)';
const textGhost = 'rgba(26,26,26,0.15)';

const svg = await satori(
  {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        flexDirection: 'column',
        width: '1200px',
        height: '630px',
        background: bone,
        padding: '0',
        position: 'relative',
        fontFamily: 'Geist Mono',
      },
      children: [
        // Outer panel border
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              top: '40px',
              left: '40px',
              right: '40px',
              bottom: '40px',
              border: `1px solid ${borderStrong}`,
              display: 'flex',
            },
          },
        },
        // Horizontal grid lines
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              top: '0',
              left: '0',
              right: '0',
              bottom: '0',
              display: 'flex',
              flexDirection: 'column',
              overflow: 'hidden',
            },
            children: [200, 350, 490].map((y) => ({
              type: 'div',
              props: {
                style: {
                  position: 'absolute',
                  top: `${y}px`,
                  left: '40px',
                  right: '40px',
                  height: '1px',
                  background: borderLight,
                },
              },
            })),
          },
        },
        // Left vertical accent line (violet)
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              left: '80px',
              top: '40px',
              bottom: '40px',
              width: '2px',
              background: violet,
              opacity: '0.4',
            },
          },
        },
        // Top-left label: // 001
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              top: '56px',
              left: '100px',
              color: textMuted,
              fontSize: '10px',
              letterSpacing: '6px',
              textTransform: 'uppercase',
              fontFamily: 'Geist Mono',
            },
            children: '// 001',
          },
        },
        // Top-right label: SOVREN SOFTWARE
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              top: '56px',
              right: '60px',
              color: textGhost,
              fontSize: '10px',
              letterSpacing: '6px',
              textTransform: 'uppercase',
              fontFamily: 'Geist Mono',
            },
            children: 'SOVREN SOFTWARE',
          },
        },
        // Main wordmark
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              top: '120px',
              left: '100px',
              right: '80px',
              display: 'flex',
              flexDirection: 'column',
              gap: '0px',
            },
            children: [
              {
                type: 'div',
                props: {
                  style: {
                    color: charcoal,
                    fontSize: '120px',
                    fontWeight: '700',
                    letterSpacing: '-2px',
                    lineHeight: '1',
                    fontFamily: 'Geist Mono',
                  },
                  children: 'SOVREN',
                },
              },
              {
                type: 'div',
                props: {
                  style: {
                    color: textGhost,
                    fontSize: '120px',
                    fontWeight: '700',
                    letterSpacing: '-2px',
                    lineHeight: '1',
                    fontFamily: 'Geist Mono',
                    marginTop: '-8px',
                  },
                  children: 'STACK.',
                },
              },
            ],
          },
        },
        // Tagline
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              bottom: '100px',
              left: '100px',
              color: textMuted,
              fontSize: '13px',
              letterSpacing: '5px',
              textTransform: 'uppercase',
              fontFamily: 'Geist Mono',
            },
            children: '> SOVEREIGN COMPUTE  ·  LOCAL IDENTITY  ·  PROGRAMMABLE CAPITAL',
          },
        },
        // Bottom domain
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              bottom: '56px',
              left: '100px',
              color: textGhost,
              fontSize: '10px',
              letterSpacing: '4px',
              fontFamily: 'Geist Mono',
            },
            children: 'SOVREN.SOFTWARE',
          },
        },
        // Right column product list with violet numbers
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              top: '56px',
              right: '60px',
              display: 'flex',
              flexDirection: 'column',
              gap: '14px',
              alignItems: 'flex-end',
              marginTop: '60px',
            },
            children: [
              { label: '01', name: 'ESVER OS' },
              { label: '02', name: 'VISAGE' },
              { label: '03', name: 'MR. HAVEN' },
            ].map(({ label, name }) => ({
              type: 'div',
              props: {
                style: {
                  display: 'flex',
                  gap: '12px',
                  alignItems: 'baseline',
                },
                children: [
                  {
                    type: 'div',
                    props: {
                      style: {
                        color: violet,
                        fontSize: '10px',
                        letterSpacing: '2px',
                        fontFamily: 'Geist Mono',
                      },
                      children: label,
                    },
                  },
                  {
                    type: 'div',
                    props: {
                      style: {
                        color: textMuted,
                        fontSize: '12px',
                        letterSpacing: '3px',
                        fontFamily: 'Geist Mono',
                      },
                      children: name,
                    },
                  },
                ],
              },
            })),
          },
        },
        // Status bar at bottom
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              bottom: '0',
              left: '0',
              right: '0',
              height: '36px',
              background: boneAlt,
              borderTop: `1px solid ${borderLight}`,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              padding: '0 60px',
            },
            children: [
              {
                type: 'div',
                props: {
                  style: {
                    color: textMuted,
                    fontSize: '9px',
                    letterSpacing: '3px',
                    fontFamily: 'Geist Mono',
                    textTransform: 'uppercase',
                  },
                  children: 'SOVREN_SOFTWARE // V1.0',
                },
              },
              {
                type: 'div',
                props: {
                  style: {
                    color: textMuted,
                    fontSize: '9px',
                    letterSpacing: '3px',
                    fontFamily: 'Geist Mono',
                    textTransform: 'uppercase',
                  },
                  children: '© 2026',
                },
              },
            ],
          },
        },
      ],
    },
  },
  {
    width: 1200,
    height: 630,
    fonts: [
      {
        name: 'Geist Mono',
        data: fontRegular,
        weight: 400,
        style: 'normal',
      },
      {
        name: 'Geist Mono',
        data: fontBold,
        weight: 700,
        style: 'normal',
      },
    ],
  }
);

const resvg = new Resvg(svg, { fitTo: { mode: 'width', value: 1200 } });
const png = resvg.render().asPng();
writeFileSync(resolve(root, 'static/og-image.png'), png);
console.log('og-image.png generated:', png.length, 'bytes');
