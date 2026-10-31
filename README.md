# Android 13 (LineageOS 20) for ASUS MeMO Pad FHD 10 LTE (ME302KL, "duma")
ENG:
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

## Installation

1. Make a backup in TWRP.
2. Flash the system image in TWRP 3.2.3.
3. Flash the kernel: fastboot flash boot boot_a13_v9.img
4. Boot into TWRP again and flash duma_firmware_a13.zip (needed for Wi-Fi, audio and sensors).
5. Reboot. The first boot takes 2-3 minutes.
6. Optional: flash duma_device_name.zip to show the model name ME302KL.
## Source (GPL-2.0)

RU:
Неофициальный порт Android 13 (LineageOS 20, сборка Nexus 7 «deb» LTE от 30.08.2023) на ASUS MeMO Pad FHD 10 LTE (ME302KL, APQ8064) с кастомным ядром 3.4 (ядро flo followmsi-13 плюс поддержка платы duma и панели Orise).

Неофициальная экспериментальная сборка. Прошивайте на свой страх и риск. Всё проверено только на одном устройстве.

Статус

Работает:
- Экран, тачскрин, Wi-Fi, звук, GPS, датчики, камеры, USB
- Система загружается и полностью пригодна для использования

Не работает / проблемы:
- Bluetooth
- microSD
- Иногда появляются синие полосы (ошибки страниц IOMMU, например при камере или выключении экрана)
- В настройках устройство всё ещё называется «Nexus 7» (есть zip для переименования)
- SELinux в режиме permissive, KCAL нет

Установка
1. Сделайте резервную копию через TWRP.
2. Прошейте образ системы в TWRP 3.2.3.
3. Прошейте ядро: fastboot flash boot boot_a13_v9.img
4. Снова загрузитесь в TWRP и прошейте duma_firmware_a13.zip (нужен для Wi-Fi, звука и датчиков).
5. Перезагрузитесь. Первая загрузка занимает 2–3 минуты.
6. По желанию: прошейте duma_device_name.zip, чтобы в настройках отображалась модель ME302KL.

Исходный код (GPL-2.0)
