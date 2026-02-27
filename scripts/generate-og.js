import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';
import { readFileSync, writeFileSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = resolve(__dirname, '..');

const fontRegular = readFileSync(resolve(root, 'node_modules/geist/dist/fonts/geist-mono/GeistMono-Regular.ttf'));
const fontBold = readFileSync(resolve(root, 'node_modules/geist/dist/fonts/geist-mono/GeistMono-Medium.ttf'));

const svg = await satori(
  {
    type: 'div',
    props: {
      style: {
        display: 'flex',
        flexDirection: 'column',
        width: '1200px',
        height: '630px',
        background: '#000000',
        padding: '0',
        position: 'relative',
        fontFamily: 'Geist Mono',
      },
      children: [
        // Grid lines — horizontal
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              bottom: '0',
              left: '0',
              right: '0',
              height: '220px',
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'flex-end',
              overflow: 'hidden',
            },
            children: [160, 120, 90, 60].map((bottom) => ({
              type: 'div',
              props: {
                style: {
                  position: 'absolute',
                  bottom: `${bottom}px`,
                  left: '0',
                  right: '0',
                  height: '1px',
                  background: 'rgba(255,255,255,0.06)',
                },
              },
            })),
          },
        },
        // Left accent bar
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              left: '60px',
              top: '60px',
              bottom: '60px',
              width: '1px',
              background: 'rgba(255,255,255,0.1)',
            },
          },
        },
        // Wireframe cube (SVG-in-Satori not supported — using box geometry)
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              top: '60px',
              left: '80px',
              width: '160px',
              height: '160px',
              border: '1.5px solid rgba(255,255,255,0.9)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            },
            children: [
              {
                type: 'div',
                props: {
                  style: {
                    width: '100px',
                    height: '100px',
                    border: '1px solid rgba(255,255,255,0.3)',
                    transform: 'rotate(15deg)',
                  },
                },
              },
            ],
          },
        },
        // Top-left label
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              top: '68px',
              left: '260px',
              color: 'rgba(255,255,255,0.3)',
              fontSize: '11px',
              letterSpacing: '4px',
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
              top: '200px',
              left: '80px',
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
                    color: '#ffffff',
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
                    color: 'rgba(255,255,255,0.15)',
                    fontSize: '120px',
                    fontWeight: '700',
                    letterSpacing: '-2px',
                    lineHeight: '1',
                    fontFamily: 'Geist Mono',
                    marginTop: '-8px',
                  },
                  children: 'SOFTWARE',
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
              left: '80px',
              color: 'rgba(255,255,255,0.4)',
              fontSize: '14px',
              letterSpacing: '6px',
              textTransform: 'uppercase',
              fontFamily: 'Geist Mono',
            },
            children: 'SOVEREIGN OS  ·  LOCAL IDENTITY  ·  PROGRAMMABLE ASSETS',
          },
        },
        // Bottom domain
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              bottom: '60px',
              left: '80px',
              color: 'rgba(255,255,255,0.18)',
              fontSize: '11px',
              letterSpacing: '3px',
              fontFamily: 'Geist Mono',
            },
            children: 'SOVREN.SOFTWARE',
          },
        },
        // Right column product list
        {
          type: 'div',
          props: {
            style: {
              position: 'absolute',
              top: '60px',
              right: '80px',
              display: 'flex',
              flexDirection: 'column',
              gap: '16px',
              alignItems: 'flex-end',
            },
            children: [
              { label: '01', name: 'AUGMENTUM OS' },
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
                        color: 'rgba(255,255,255,0.2)',
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
                        color: 'rgba(255,255,255,0.5)',
                        fontSize: '13px',
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
