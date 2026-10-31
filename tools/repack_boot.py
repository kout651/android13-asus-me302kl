#!/usr/bin/env python3
"""Replace the kernel inside an Android boot.img (header v0), keep ramdisk and parameters.
Usage: python repack_boot.py old_boot.img zImage new_boot.img [--cmdline "..."]"""
import sys, struct, hashlib

def pad(n, page): return (page - (n % page)) % page

def main():
    a = sys.argv[1:]
    if len(a) < 3: sys.exit(__doc__)
    old, kfile, new = a[:3]
    cmd = a[a.index('--cmdline')+1] if '--cmdline' in a else None
    d = open(old, 'rb').read()
    if d[:8] != b'ANDROID!': sys.exit('not an Android boot.img')
    (ksz, kaddr, rsz, raddr, ssz, saddr, taddr, page, dtsz, unused) = struct.unpack('<10I', d[8:48])
    name = d[48:64]; cmdline = d[64:576]; extra = d[608:1632]
    if cmd is not None: cmdline = cmd.encode().ljust(512, b'\0')
    off = page
    kernel = d[off:off+ksz]; off += ksz + pad(ksz, page)
    ramdisk = d[off:off+rsz]; off += rsz + pad(rsz, page)
    second = d[off:off+ssz]; off += ssz + pad(ssz, page)
    dt = d[off:off+dtsz]
    print('old kernel %d, ramdisk %d, page %d, base-ish kaddr %#x' % (ksz, rsz, page, kaddr))
    print('cmdline:', cmdline.split(b'\0')[0].decode(errors='replace'))
    nk = open(kfile, 'rb').read()
    sha = hashlib.sha1()
    for blob in (nk, ramdisk, second, dt if dtsz else b''):
        sha.update(blob); sha.update(struct.pack('<I', len(blob)))
    ident = sha.digest().ljust(32, b'\0')
    hdr = b'ANDROID!' + struct.pack('<10I', len(nk), kaddr, rsz, raddr, ssz, saddr, taddr, page, dtsz, unused)
    hdr += name + cmdline + ident + extra
    out = hdr + b'\0' * pad(len(hdr), page)
    for blob in (nk, ramdisk, second, dt):
        if blob: out += blob + b'\0' * pad(len(blob), page)
    open(new, 'wb').write(out)
    print('wrote', new, len(out), 'bytes; new kernel', len(nk))
main()
