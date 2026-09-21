# 📖 man.ua — Українська системна документація та довідник Man-Pages

[![CachyOS Linux](https://img.shields.io/badge/OS-CachyOS%20Linux-00acc1?style=flat-square&logo=linux)](https://cachyos.org)
[![Ubuntu](https://img.shields.io/badge/OS-Ubuntu%20%2F%20Debian-e95420?style=flat-square&logo=ubuntu)](https://ubuntu.com)
[![Language](https://img.shields.io/badge/Language-Українська%20(UK)-blue?style=flat-square)](https://github.com)
[![Sections](https://img.shields.io/badge/Man%20Sections-1%20to%209-10b981?style=flat-square)](https://man7.org)
[![Pages Count](https://img.shields.io/badge/Pages-34%20000%2B-purple?style=flat-square)](https://github.com/AndreyVeremchuck/man.ua)
[![Web Catalog](https://img.shields.io/badge/Web%20Catalog-ua%2Findex.html-emerald?style=flat-square)](ua/index.html)
[![License](https://img.shields.io/badge/License-GPL%20%2F%20MIT-amber?style=flat-square)](LICENSE)

> **`man.ua`** — це відкритий репозиторій, системна бібліотека та інтерактивний вебкалендар перекладу понад **34 000 сторінок документації Linux man-pages** українською мовою.

---

## 🌐 Інтерактивний перегляд у браузері (`ua/index.html`)

У репозиторії створено спеціальний автономний **веб-каталог посібників**, який відкривається в один клік у будь-якому браузері (Chrome, Firefox тощо) без потреби у вебсервері:

* 📱 **Локальне відкриття**: [`ua/index.html`](ua/index.html) (або `xdg-open ua/index.html`).
* 🔍 **Миттєвий живий пошук** за назвою утиліти, системним викликом чи описом.
* 🗂️ **Фільтрація за 9 розділами** системного посібника.
* 📋 **Копіювання синтаксису та прикладів** в один клік.
* 📄 **Markdown-версії посібників** у каталозі [`ua/`](ua/README.md).

---

## ⚡ Швидке встановлення в систему (1 команда)

Якщо ви клонували репозиторій і бажаєте встановити всі 34 000+ посібників у систему:

```bash
git clone https://github.com/AndreyVeremchuck/man.ua.git
cd man.ua

# Автоматичне встановлення всіх розділів (man/man1–man9) та оновлення бази mandb:
sudo ./install.sh

# Або класично через Makefile:
sudo make install
```

---

## 📁 Реальна структура репозиторію

Усі вихідні системні посібники зібрано всередині каталогу `man/`, а вебкалендар та Markdown-документацію — у `ua/`:

```
man.ua/
├── man/                     # 📦 Всі вихідні системні man-файли (34 000+ сторінок):
│   ├── man1/                # 4 566 файлів: Користувацькі програми (ls, grep, intro, tar, git)
│   ├── man2/                # 1 077 файлів: Системні виклики ядра Linux (open, read, fork, clone)
│   ├── man3/                # 25 845 файлів: Бібліотеки C/libc, POSIX та Wayland C API
│   ├── man4/                # 47 файлів: Спеціальні файли та пристрої (/dev/null, tty, random)
│   ├── man5/                # 730 файлів: Формати конфігураційних файлів (/etc/passwd, fstab)
│   ├── man6/                # 4 файли: Ігри та розваги (sl, fortune, bsd-games)
│   ├── man7/                # 763 файли: Стандарти, протоколи та огляди (ip, tcp, hier, man-pages)
│   ├── man8/                # 1 374 файли: Команди системного адміністрування (systemctl, btrfs, iptables)
│   └── man9/                # 1 файл: Внутрішні процедури ядра Linux
├── ua/                      # 🌐 Веб-каталог та Markdown-посібники для читання в браузері:
│   ├── index.html           # Інтерактивний веб-каталог SPA (пошук, фільтри, копіювання)
│   ├── README.md            # Навігатор за Markdown-посібниками
│   ├── man1/ ... man8/      # Структуровані Markdown (.md) файли для читання на GitHub
├── assets/                  # Скріншоти та візуалізації терміналу
│   ├── man_man.png          # Скріншот виклику `man man`
│   └── man_intro.png        # Скріншот виклику `man intro`
├── install.sh               # Скрипт автоматичного розгортання в /usr/share/man/uk/
├── uninstall.sh             # Скрипт чистого видалення
├── Makefile                 # Встановлення через `sudo make install` / `uninstall`
├── build_ua_catalog.py      # Генератор веб-каталогу та Markdown-файлів
├── generate_screenshots.py  # Генератор термінальних скріншотів
├── README.md                # Головний посібник користувача
└── .gitignore               # Конфігурація Git
```

---

## 📚 Розділи системного посібника (Man-Pages Sections 1–9)

| Розділ | Категорія | Кількість | Опис призначення | Приклади виклику |
| :---: | :--- | :---: | :--- | :--- |
| **1** | **Виконувані програми та команди оболонки** | **4 566** | Користувацькі утиліти, бінарні програми, інструменти обробки тексту, компілятори та командні оболонки. | `man 1 ls`<br>`man 1 grep`<br>`man 1 intro`<br>`man 1 tar` |
| **2** | **Системні виклики ядра Linux** | **1 077** | Функції ядра Linux, що забезпечують пряму взаємодію між простором користувача (user-space) та ядром (kernel-space). | `man 2 open`<br>`man 2 read`<br>`man 2 fork`<br>`man 2 clone` |
| **3** | **Бібліотечні виклики C / libc / POSIX API** | **25 845** | Функції стандартної бібліотеки мови C (`glibc`, `musl`) та системних бібліотек (`libwayland`, `libcurl`, `pthreads`). | `man 3 printf`<br>`man 3 malloc`<br>`man 3 wl_display_connect`<br>`man 3 pthread_create` |
| **4** | **Спеціальні файли та пристрої (`/dev`)** | **47** | Інтерфейси драйверів пристроїв, віртуальні та символьні пристрої у файловій системі. | `man 4 null`<br>`man 4 tty`<br>`man 4 random`<br>`man 4 loop` |
| **5** | **Формати конфігураційних файлів та угоди** | **730** | Синтаксис та правила оформлення системних конфігураційних файлів (`/etc/*`), баз даних та форматів файлів. | `man 5 passwd`<br>`man 5 fstab`<br>`man 5 crontab`<br>`man 5 systemd.unit` |
| **6** | **Ігри та розваги** | **4** | Текстові та графічні консольні ігри, генератори заставок, анімації та розважальні програми. | `man 6 sl`<br>`man 6 fortune`<br>`man 6 bsd-games`<br>`man 6 factor` |
| **7** | **Огляди, конвенції, стандарти та макроси** | **763** | Оглядові статті, мережеві протоколи, таблиці кодувань, стандарти POSIX, структура ФС та макропакети (`groff`). | `man 7 ip`<br>`man 7 tcp`<br>`man 7 hier`<br>`man 7 utf-8`<br>`man 7 man-pages` |
| **8** | **Команди системного адміністрування** | **1 374** | Утиліти керування службами, демонами, дисковими розділами, мережею та безпекою (зазвичай вимагають привілеїв `root`). | `man 8 systemctl`<br>`man 8 btrfs`<br>`man 8 fdisk`<br>`man 8 iptables`<br>`man 8 pacman` |
| **9** | **Внутрішні підпрограми ядра Linux** | **1** | Нестандартний розділ документації внутрішніх інтерфейсів ядра, підсистем та модулів розробки драйверів. | `man 9 kmalloc`<br>`man 9 sk_buff` |

---

## 🛠️ Налаштування та системні вимоги (CachyOS vs Ubuntu)

### 1. ⚡ CachyOS / Arch Linux
```bash
# 1. Встановлення man-db:
sudo pacman -S man-db man-pages

# 2. Генерація локалі (розкоментувати uk_UA.UTF-8 UTF-8 у /etc/locale.gen):
sudo locale-gen

# 3. Встановлення сторінок:
sudo ./install.sh
```

### 2. 🐧 Ubuntu / Debian Linux
```bash
# 1. Встановлення базових пакетів:
sudo apt update
sudo apt install man-db manpages

# 2. Генерація локалі:
sudo locale-gen uk_UA.UTF-8
sudo update-locale LANG=uk_UA.UTF-8

# 3. Встановлення сторінок:
sudo ./install.sh
```

---

### 🔄 Порівняльна таблиця відмінностей: CachyOS vs Ubuntu

| Характеристика | ⚡ CachyOS (Arch-based) | 🐧 Ubuntu / Debian |
| :--- | :--- | :--- |
| **Пакетний менеджер** | `pacman` / `paru` / `yay` | `apt` |
| **Формат стиснення сторінок** | `.gz` / `.zst` | `.gz` |
| **Файл конфігурації локалей** | `/etc/locale.gen` + `locale-gen` | `/etc/default/locale` + `update-locale` |
| **Каталог зберігання сторінок** | `/usr/share/man/uk/` | `/usr/share/man/uk/` |
| **Команда оновлення індексу** | `sudo mandb` | `sudo mandb -c` |

---

### 💡 Як примусово відкривати українську версію (`man -L uk`)

Якщо основна мова вашої системи встановлена англійською (`LANG=en_US.UTF-8`), ви можете відкривати українські сторінки прапорцем `-L uk` або створити аліас:

* **Разовий виклик**:
  ```bash
  man -L uk intro
  man -L uk 1 ls
  man -L uk 3 wl_display_connect
  ```

* **Створення аліасу `uman` (для Fish / Bash / Zsh)**:
  ```bash
  # Для Fish (~/.config/fish/config.fish):
  alias uman="man -L uk"

  # Для Bash/Zsh (~/.bashrc або ~/.zshrc):
  alias uman='man -L uk'
  ```

---

## 🖼️ Візуалізація терміналу та скріншоти

### 1. 📟 Посібник посібників: `man man`
![Скріншот man man](assets/man_man.png)

---

### 2. 🔰 Вступ до команд користувача: `man intro` (`man 1 intro`)
![Скріншот man intro](assets/man_intro.png)

---

## ⚡ Швидка шпаргалка роботи з `man`

```bash
# 1. Відкрити посібник для команди:
man ls

# 2. Відкрити посібник із конкретного розділу:
man 1 printf   # Команда оболонки printf
man 3 printf   # C-функція бібліотеки libc printf()

man 2 read     # Системний виклик ядра read()
man 1 read     # Вбудована команда оболонки read

# 3. Пошук за ключовими словами в описах (аналог apropos):
man -k "пошук файлів"
man -k network

# 4. Короткий опис команди (аналог whatis):
man -f grep

# 5. Дізнатися шлях до файлу man-сторінки:
man -w btrfs
man -w 3 wl_display_connect
```

---

## 🤝 Як долучитися до розвитку

1. Створіть форк репозиторію.
2. Додайте або покращіть переклад man-сторінки у відповідний розділ (`man/man1/` ... `man/man9/` або `ua/`).
3. Перевірте форматування за допомогою `man -l <шлях_до_файлу>`.
4. Надішліть Pull Request!

---

*Зроблено в Україні з любов'ю до відкритого коду та Linux.* 🇺🇦
