#!/usr/bin/env python3
"""
Build-Script für KS Pitch Deck.
Liest shared/header.html + slides/*.html + shared/footer.html
und schreibt index.html.

Usage: python3 build.py
"""
import os, glob

BASE = os.path.dirname(os.path.abspath(__file__))
HEADER = os.path.join(BASE, 'shared', 'header.html')
FOOTER = os.path.join(BASE, 'shared', 'footer.html')
SLIDES_DIR = os.path.join(BASE, 'slides')
OUT = os.path.join(BASE, 'index.html')

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    # Slides sortiert nach Dateiname (01-, 02-, ...)
    slide_files = sorted(glob.glob(os.path.join(SLIDES_DIR, '*.html')))
    
    print(f"Build: {len(slide_files)} Slides")
    
    parts = [read(HEADER)]
    for sf in slide_files:
        slide_html = read(sf).rstrip() + '\n\n'
        parts.append(slide_html)
        size = os.path.getsize(sf)
        print(f"  {os.path.basename(sf):30s}  {size:>8,} chars")
    parts.append(read(FOOTER))
    
    output = ''.join(parts)
    
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"\n✓ {OUT}  ({len(output):,} chars)")

if __name__ == '__main__':
    main()
