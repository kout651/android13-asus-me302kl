# Android 13 (LineageOS 20) for ASUS MeMO Pad FHD 10 LTE (ME302KL, "duma")

[Русская версия](README.ru.md)

Unofficial port of Android 13 (LineageOS 20, Nexus 7 "deb" LTE build 2023-08-30) to the ASUS MeMO Pad FHD 10 LTE (ME302KL, APQ8064), running on a custom 3.4 kernel (flo followmsi-13 kernel + duma board / Orise panel support).

> Unofficial and experimental. Flash at your own risk. Everything is tested on one device only.

## Status

**Working:** display, touch, Wi-Fi, audio, GPS, sensors, cameras, USB. Boots to a fully usable system.

**Not working / known issues:**
- Bluetooth
- microSD
- Occasional blue stripes (IOMMU page faults, e.g. camera / screen off). A short press of the power button helps
- Device still shown as "Nexus 7" in Settings (rename zip provided)
- SELinux permissive, no KCAL (color calibration)

## Installation (Windows, fastboot + TWRP 3.2.3)

1. Make a backup in TWRP.
2. Flash the system image in TWRP 3.2.3.
3. Flash the kernel: `fastboot flash boot boot_a13_v9.img`
4. Boot into TWRP again and flash `duma_firmware_a13.zip` (needed for Wi-Fi, audio and sensors).
5. Reboot. The first boot takes 2-3 minutes.
6. Optional: flash `duma_device_name.zip` to show the model name ME302KL.

Downloads are on the Releases page.

## Source code (GPL-2.0)

- `kernel/duma-on-flo-kernel-v9.patch` - kernel changes (diff against the flo followmsi-13 kernel, Linux 3.4)
- `kernel/duma_v9.config` - kernel config used for the v9 build
- `tools/repack_boot.py` - replaces only the kernel inside a boot.img
- `tools/make_system_img.py` - builds system.img from a LineageOS OTA zip

## Credits and thanks

- **LineageOS** team - the base system (LineageOS 20, Nexus 7 "deb" build)
- **retiredtab** - Android 13 for Nexus 7 and the flo kernel (followmsi-13 branch)
- **followmsi** - flo kernel work
- **yatto / ElementalX** - duma kernel (GPL-2.0), the source of the board support
- **ASUS** - original duma kernel and firmware sources
- **4PDA community** - testing and feedback, in particular the ME302KL thread
- **Claude (Anthropic)** - kernel porting assistance (board/panel/touch support, debugging)

Port and testing by **xiamist** (kout651).

## License

Kernel changes are GPL-2.0, like the Linux kernel. LineageOS and Android components keep their original licenses (Apache-2.0 and others). This is not an official LineageOS build.
