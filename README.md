# Android 13 (LineageOS 20) for ASUS MeMO Pad FHD 10 LTE (ME302KL, "duma")

Unofficial port of Android 13 (LineageOS 20, Nexus 7 "deb" LTE build 2023-08-30) to the ASUS MeMO Pad FHD 10 LTE (ME302KL, APQ8064), running on a custom 3.4 kernel (flo followmsi-13 kernel + duma board / Orise panel support).

> Unofficial and experimental. Flash at your own risk. Everything is tested on one device only.

## Status

| Works | Not working / issues |
|---|---|
| Display, touch, Wi-Fi, audio, GPS, sensors, cameras, USB | Bluetooth |
| Boots to a fully usable system | microSD |
| | Occasional blue stripes (IOMMU page faults, e.g. camera/screen-off) |
| | Device still shown as "Nexus 7" in Settings (rename zip provided) |
| | SELinux permissive, no KCAL |

## Install (Windows, fastboot + TWRP 3.2.3)

1. Flash the Android 13 system and boot image (`boot_a13_v9.img`) from the Releases page.
2. In TWRP flash `duma_firmware_a13.zip` (Wi-Fi, audio, sensors firmware from LineageOS 17.1 duma).
3. Optional: flash `duma_device_name.zip` to set the model name to ME302KL.

## Source (GPL-2.0)
