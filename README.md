# Android 13 (LineageOS 20) for ASUS MeMO Pad FHD 10 LTE (ME302KL, "duma")
ENG:
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

RU:
# Android 13 (LineageOS 20) для ASUS MeMO Pad FHD 10 LTE (ME302KL, «duma»)

[English](README.md)

Неофициальный порт Android 13 (LineageOS 20, сборка Nexus 7 «deb» LTE от 30.08.2023) на ASUS MeMO Pad FHD 10 LTE (ME302KL, APQ8064) с кастомным ядром 3.4 (ядро flo followmsi-13 плюс поддержка платы duma и панели Orise).

> Неофициальная экспериментальная сборка. Прошивайте на свой страх и риск. Всё проверено только на одном устройстве.

## Статус

**Работает:** экран, тачскрин, Wi-Fi, звук, GPS, датчики, камеры, USB. Система загружается и полностью пригодна для использования.

**Не работает / известные проблемы:**
- Bluetooth
- microSD
- Иногда появляются синие полосы (ошибки страниц IOMMU, например при камере или выключении экрана). Помогает короткое нажатие кнопки питания
- В настройках устройство всё ещё называется «Nexus 7» (есть zip для переименования)
- SELinux в режиме permissive, нет KCAL (цветокоррекции)

## Установка (Windows, fastboot + TWRP 3.2.3)

1. Сделайте резервную копию через TWRP.
2. Прошейте образ системы в TWRP 3.2.3.
3. Прошейте ядро: `fastboot flash boot boot_a13_v9.img`
4. Снова загрузитесь в TWRP и прошейте `duma_firmware_a13.zip` (нужен для Wi-Fi, звука и датчиков).
5. Перезагрузитесь. Первая загрузка занимает 2–3 минуты.
6. По желанию: прошейте `duma_device_name.zip`, чтобы отображалась модель ME302KL.

Файлы для скачивания на странице Releases.

## Исходный код (GPL-2.0)

- `kernel/duma-on-flo-kernel-v9.patch` — изменения ядра (diff относительно ядра flo followmsi-13, Linux 3.4)
- `kernel/duma_v9.config` — конфиг ядра сборки v9
- `tools/repack_boot.py` — заменяет только ядро внутри boot.img
- `tools/make_system_img.py` — собирает system.img из OTA-архива LineageOS

## Благодарности

- Команда **LineageOS** — основа системы (LineageOS 20, сборка Nexus 7 «deb»)
- **retiredtab** — Android 13 для Nexus 7 и ядро flo (ветка followmsi-13)
- **followmsi** — работа над ядром flo
- **yatto / ElementalX** — ядро duma (GPL-2.0), источник поддержки платы
- **ASUS** — исходники оригинального ядра и прошивки duma
- Сообщество **4PDA** — тестирование и отзывы, особенно в теме ME302KL
- **Claude (Anthropic)** — помощь в портировании ядра (плата, панель, тачскрин, отладка)

Порт и тестирование: **xiamist** (kout651).

## Лицензия

Изменения ядра распространяются под GPL-2.0, как и ядро Linux. Компоненты LineageOS и Android сохраняют исходные лицензии (Apache-2.0 и другие). Это не официальная сборка LineageOS.

