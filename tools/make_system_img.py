#!/usr/bin/env python3
"""Build a raw system.img from a LineageOS recovery zip (system.new.dat.br).
Usage:  python make_system_img.py lineage-20.0-...-deb.zip system.img
Needs: Python 3 and the 'brotli' module (pip install brotli)."""
import sys, zipfile, re, os, io, tempfile

BS = 4096

def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    zpath, out = sys.argv[1], sys.argv[2]
    z = zipfile.ZipFile(zpath)
    tl = z.read('system.transfer.list').decode().split('\n')
    ver = int(tl[0]); total = int(tl[1])
    if ver < 2:
        sys.exit('unsupported transfer list version %d' % ver)
    erase_end = 0
    new_cmds = []
    for line in tl[4:]:
        line = line.strip()
        if not line:
            continue
        cmd, rest = line.split(' ', 1)
        a = list(map(int, rest.split(',')))
        if cmd == 'new':
            new_cmds.append([(a[i], a[i + 1]) for i in range(1, len(a), 2)])
        elif cmd == 'erase':
            erase_end = max(erase_end, max(a[2::2]))
        elif cmd in ('move', 'bsdiff', 'imgdiff'):
            sys.exit('this zip is an incremental update (%s): not supported' % cmd)
    try:
        import brotli
    except ImportError:
        sys.exit("Install the brotli module first:  pip install brotli")
    dec = brotli.Decompressor()
    src = z.open('system.new.dat.br')

    def blocks():
        while True:
            chunk = src.read(1 << 20)
            if not chunk:
                break
            data = dec.process(chunk)
            if data:
                yield data

    buf = bytearray()
    it = blocks()

    def read(n):
        nonlocal buf
        while len(buf) < n:
            try:
                buf += next(it)
            except StopIteration:
                break
        r = bytes(buf[:n]); del buf[:n]
        return r

    with open(out, 'wb') as o:
        for ranges in new_cmds:
            for s, e in ranges:
                o.seek(s * BS)
                n = (e - s) * BS
                while n > 0:
                    b = read(min(n, 16 << 20))
                    if not b:
                        sys.exit('data ended early: zip damaged?')
                    o.write(b); n -= len(b)
        final = max(total, erase_end) * BS
        o.truncate(final)
    print('done:', out, os.path.getsize(out), 'bytes')

main()
