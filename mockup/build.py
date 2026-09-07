#!/usr/bin/env python3
"""Assemble mockup/index.html from src/index.html, inlining the desktop screenshot.

{{IMG:desktop}} is replaced with a base64 data URI of the committed Windows 11
screenshot, so the published mockup is a single self-contained file.
"""
import base64, io, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)
SHOT = os.path.join(REPO, 'Windows_11_Desktop_bee0wa.webp')

if not os.path.exists(SHOT):
    sys.exit('missing screenshot: ' + SHOT)

src = io.open(os.path.join(ROOT, 'src', 'index.html'), encoding='utf-8').read()
uri = 'data:image/webp;base64,' + base64.b64encode(open(SHOT, 'rb').read()).decode('ascii')
out = src.replace('{{IMG:desktop}}', uri)
if '{{IMG:' in out:
    sys.exit('unresolved placeholder in src/index.html')

io.open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(out)
print('mockup/index.html  %.1f KB' % (len(out.encode('utf-8')) / 1024.0))
