Kernel changes for ASUS MeMO Pad FHD 10 LTE (ME302KL, duma) on top of
retiredtab's flo kernel (followmsi-13 branch, Linux 3.4).

duma-on-flo-kernel-v9.patch  - source changes (apply with: git apply on the flo kernel tree)
duma_v9.config               - kernel config used for the v9 build
repack_boot.py               - replaces only the kernel inside a boot.img
make_system_img.py           - builds system.img from a LineageOS OTA zip

Based on: retiredtab flo kernel, yatto/ElementalX duma kernel (GPL-2.0).
