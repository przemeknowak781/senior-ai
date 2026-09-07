#!/usr/bin/env python3
"""Assemble deck/index.html from src/shell.html + src/slides.html, inlining screenshots.

Placeholders {{IMG:name}} in slides.html are replaced with a base64 data URI built
from assets/<name>.jpg, so the published deck is a single self-contained file.
"""
import base64, io, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
shell = io.open(os.path.join(ROOT, 'src', 'shell.html'), encoding='utf-8').read()
slides = io.open(os.path.join(ROOT, 'src', 'slides.html'), encoding='utf-8').read()

missing = []
def img(m):
    name = m.group(1)
    path = os.path.join(ROOT, 'assets', name + '.jpg')
    if not os.path.exists(path):
        missing.append(name); return ''
    data = base64.b64encode(open(path, 'rb').read()).decode('ascii')
    return 'data:image/jpeg;base64,' + data

slides = re.sub(r'\{\{IMG:([a-z0-9_-]+)\}\}', img, slides)
if missing:
    sys.exit('missing assets: ' + ', '.join(sorted(set(missing))))

out = shell.replace('<!--SLIDES-->', slides)
io.open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(out)
n = out.count('class="slide')
print('deck/index.html  %.1f KB  %d slides' % (len(out.encode('utf-8')) / 1024.0, n))
