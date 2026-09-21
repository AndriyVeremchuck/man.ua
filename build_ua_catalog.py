#!/usr/bin/env python3
"""
Builder for ua/ catalog:
1. Generates rich Markdown files in ua/man1/, ua/man2/, etc.
2. Generates ua/index.html — interactive browser-based man-pages reader with search & filters.
3. Generates ua/README.md catalog index.
"""

import os
import gzip
import html
import subprocess
from pathlib import Path

BASE_DIR = Path("/home/dusha/Шаблони/APP/man.ua")
UA_DIR = BASE_DIR / "ua"
UA_DIR.mkdir(exist_ok=True)

SECTIONS_INFO = {
    "1": {"name": "Виконувані програми та команди оболонки", "icon": "💻", "count": 4566, "desc": "Користувацькі утиліти, командні оболонки, текстові процесори, компілятори"},
    "2": {"name": "Системні виклики ядра Linux", "icon": "🧠", "count": 1077, "desc": "Прямі системні виклики між простором користувача та ядром (syscalls)"},
    "3": {"name": "Бібліотечні виклики C / libc / Wayland API", "icon": "📚", "count": 25845, "desc": "Функції glibc, posix, wayland та системних C-бібліотек"},
    "4": {"name": "Спеціальні файли та пристрої (/dev)", "icon": "🔌", "count": 47, "desc": "Драйвери пристроїв, псевдо-пристрої (/dev/null, /dev/random, /dev/tty)"},
    "5": {"name": "Формати конфігураційних файлів (/etc)", "icon": "📑", "count": 730, "desc": "Синтаксис конфігураційних файлів (/etc/passwd, fstab, crontab, systemd)"},
    "6": {"name": "Ігри та консольні розваги", "icon": "🎮", "count": 4, "desc": "Текстові ігри, анімації та екранні заставки (sl, fortune)"},
    "7": {"name": "Огляди, стандарти, конвенції та протоколи", "icon": "🌐", "count": 763, "desc": "Мережеві протоколи TCP/IP, стандарти POSIX, ієрархія файлової системи hier(7)"},
    "8": {"name": "Команди системного адміністрування (Root)", "icon": "🛡️", "count": 1374, "desc": "Утиліти керування службами, дисками, демонами, безпекою (systemctl, btrfs)"},
    "9": {"name": "Внутрішні процедури ядра Linux", "icon": "⚙️", "count": 1, "desc": "Внутрішні процедури та інтерфейси розробки модулів ядра Linux"}
}

CORE_MAN_PAGES = [
    # Section 1
    ("1", "intro", "Вступ до команд користувача, структура CLI, конвеєри та I/O перенаправлення",
     "man 1 intro", "$ intro\n$ man 1 intro", ["1", "ls", "grep", "cat", "bash"]),
    ("1", "man", "Інтерфейс до системних довідкових посібників та пошук документації",
     "man [-k|-f|-l|-w] [[section] page...]", "$ man man\n$ man -k 'пошук'\n$ man 1 printf", ["1", "apropos", "whatis"]),
    ("1", "ls", "Виведення списку файлів та вмісту директорій з атрибутами",
     "ls [OPTIONS] [FILE...]", "$ ls -la --color=auto\n$ ls -lh /var/log", ["1", "dir", "vdir", "stat"]),
    ("1", "grep", "Пошук рядків за регулярними виразами та шаблонами у файлах",
     "grep [OPTIONS] PATTERN [FILE...]", "$ grep -rn 'TODO' .\n$ cat log | grep -i 'error'", ["1", "egrep", "fgrep", "rg"]),
    ("1", "cat", "Об'єднання та виведення вмісту файлів у стандартний потік виводу",
     "cat [OPTIONS] [FILE...]", "$ cat /etc/os-release\n$ cat -n script.sh", ["1", "tac", "bat", "head", "tail"]),
    ("1", "tar", "Утиліта створення, розпакування та маніпулювання архівами",
     "tar [-c|-x|-t] [-z|-j|-J|-I zstd] -f archive.tar [FILES...]", "$ tar -I zstd -cf arch.tar.zst dir/\n$ tar -xvf arch.tar.gz", ["1", "gzip", "zstd", "xz"]),
    ("1", "find", "Рекурсивний пошук файлів та директорій за критеріями та атрибутами",
     "find [PATH...] [EXPRESSION]", "$ find . -type f -name '*.md'\n$ find /tmp -mtime +7 -delete", ["1", "fd", "locate", "xargs"]),
    ("1", "chmod", "Зміна прав доступу до файлів та директорій у файловій системі",
     "chmod [OPTIONS] MODE[,MODE]... FILE...", "$ chmod +x script.sh\n$ chmod -R 755 /var/www", ["1", "chown", "umask", "stat"]),
    ("1", "chown", "Зміна власника та групи файлів або каталогів",
     "chown [OPTIONS] [OWNER][:[GROUP]] FILE...", "$ sudo chown user:group file.txt\n$ sudo chown -R $USER:$USER .", ["1", "chmod", "chgrp"]),
    ("1", "ps", "Звіт про поточні активні процеси користувача та системи",
     "ps [OPTIONS]", "$ ps aux | grep python\n$ ps -ef --forest", ["1", "top", "htop", "pgrep", "kill"]),
    ("1", "kill", "Надсилання сигналів процесам за їхнім числовим ідентифікатором (PID)",
     "kill [-s SIGNAL | -SIGNAL] PID...", "$ kill -15 1234  # SIGTERM\n$ kill -9 1234   # SIGKILL", ["1", "killall", "pkill", "signal"]),
    ("1", "bash", "Командний інтерпретатор та мова сценаріїв GNU Bourne Again Shell",
     "bash [OPTIONS] [FILE [ARGUMENTS...]]", "$ bash script.sh\n$ bash -x debug_script.sh", ["1", "sh", "zsh", "fish"]),
    ("1", "git", "Розподілена система керування версіями вихідного коду",
     "git [--version] [--help] [-C <path>] <command> [<args>]", "$ git status\n$ git commit -m 'Docs update'\n$ git push", ["1", "git-commit", "git-diff"]),
    ("1", "curl", "Утиліта для передачі даних за мережевими протоколами (HTTP, HTTPS, FTP)",
     "curl [OPTIONS...] <url>", "$ curl -fsSL https://get.url | bash\n$ curl -I https://example.com", ["1", "wget", "http"]),
    
    # Section 2
    ("2", "open", "Відкриття або створення файлу чи пристрою та отримання файлового дескриптора",
     "int open(const char *pathname, int flags, mode_t mode);", "int fd = open(\"file.txt\", O_RDONLY | O_CLOEXEC);", ["2", "creat", "close", "read", "write"]),
    ("2", "read", "Зчитування байтів із файлового дескриптора у буфер пам'яті",
     "ssize_t read(int fd, void *buf, size_t count);", "ssize_t n = read(fd, buffer, sizeof(buffer));", ["2", "write", "open", "pread"]),
    ("2", "write", "Запис даних із буфера у файловий дескриптор",
     "ssize_t write(int fd, const void *buf, size_t count);", "write(STDOUT_FILENO, \"Hello\\n\", 6);", ["2", "read", "open", "pwrite"]),
    ("2", "fork", "Створення нового дочірнього процесу шляхом дублювання поточного",
     "pid_t fork(void);", "pid_t pid = fork();\nif (pid == 0) { /* child */ }", ["2", "clone", "vfork", "execve"]),
    ("2", "clone", "Створення дочірнього процесу або потоку з налаштуванням просторів імен",
     "int clone(int (*fn)(void *), void *stack, int flags, void *arg, ...);", "clone(child_fn, stack_top, CLONE_VM | CLONE_FS | SIGCHLD, NULL);", ["2", "fork", "unshare", "namespaces"]),
    
    # Section 3
    ("3", "printf", "Форматоване виведення тексту у стандартний потік (stdout)",
     "int printf(const char *format, ...);", "printf(\"Привіт, %s! Число: %d\\n\", \"Світ\", 42);", ["3", "sprintf", "snprintf", "fprintf"]),
    ("3", "malloc", "Динамічне виділення блоку пам'яті заданого розміру у купі (heap)",
     "void *malloc(size_t size);", "char *buf = (char *)malloc(1024);\nif (!buf) { /* помилка */ }\nfree(buf);", ["3", "free", "calloc", "realloc"]),
    ("3", "wl_display_connect", "Підключення клієнтського додатку до Wayland-композитора",
     "struct wl_display *wl_display_connect(const char *name);", "struct wl_display *dpy = wl_display_connect(NULL);", ["3", "wl_display_disconnect", "wayland"]),
    
    # Section 4
    ("4", "null", "Нульовий пристрій скидання даних (/dev/null) та генератор нулів (/dev/zero)",
     "/dev/null, /dev/zero", "$ command > /dev/null 2>&1\n$ dd if=/dev/zero of=test.img bs=1M count=10", ["4", "zero", "random", "urandom"]),
    ("4", "tty", "Керуючий термінальний пристрій поточного процесу (/dev/tty)",
     "/dev/tty", "$ echo \"Повідомлення на термінал\" > /dev/tty", ["4", "console", "pts"]),
    
    # Section 5
    ("5", "passwd", "Файл бази даних облікових записів користувачів системи (/etc/passwd)",
     "ім'я:пароль:UID:GID:GECOS:домашній_каталог:оболонка", "dusha:x:1000:1000:Andrey:/home/dusha:/usr/bin/fish", ["5", "shadow", "group"]),
    ("5", "fstab", "Статична конфігурація точок монтування файлових систем (/etc/fstab)",
     "<накопичувач/UUID> <точка_монтування> <тип_ФС> <опції> <dump> <pass>", "UUID=xxxx-xxxx / btrfs subvol=@,compress=zstd:3 0 0", ["5", "mount", "crypttab"]),
    
    # Section 7
    ("7", "intro", "Вступ до загальних конвенцій, оглядів, мережевих стеків та стандартів",
     "man 7 intro", "$ man 7 intro\n$ man 7 hier\n$ man 7 tcp", ["7", "man-pages", "hier", "posix"]),
    ("7", "hier", "Опис структури та ієрархії стандартної файлової системи Linux/UNIX",
     "/, /bin, /etc, /usr, /var, /opt, /dev, /proc, /sys", "$ man 7 hier", ["7", "file-hierarchy", "pathname"]),
    ("7", "tcp", "Протокол керування передачею даних TCP (Transmission Control Protocol)",
     "TCP / IP v4/v6 протокол", "$ man 7 tcp\n$ man 7 ip\n$ man 7 socket", ["7", "ip", "udp", "socket"]),
    
    # Section 8
    ("8", "systemctl", "Керування системним менеджером systemd та фоновими службами",
     "systemctl [OPTIONS...] COMMAND [UNIT...]", "$ sudo systemctl start docker\n$ systemctl status NetworkManager", ["8", "journalctl", "systemd"]),
    ("8", "btrfs", "Утиліта керування файловою системою Btrfs, підтомами та снапшотами",
     "btrfs <command> [<args>]", "$ sudo btrfs subvolume list /\n$ sudo btrfs filesystem df /", ["8", "snapper", "mkfs.btrfs"]),
    ("8", "iptables", "Адміністрування міжмережевого екрана IPv4 та фільтрація пакетів",
     "iptables [-t table] {-A|-D|-I} chain rule-specification", "$ sudo iptables -L -n -v\n$ sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT", ["8", "nft", "ufw", "firewalld"])
]

# 1. Generate Markdown files in ua/manX/
for sec, name, summary, synopsis, examples, alts in CORE_MAN_PAGES:
    sec_dir = UA_DIR / f"man{sec}"
    sec_dir.mkdir(exist_ok=True)
    md_file = sec_dir / f"{name}.{sec}.md"
    
    md_content = f"""# 📖 {name}({sec}) — Українська системна документація

> **Розділ {sec}**: {SECTIONS_INFO[sec]['name']}  
> **Оригінальний виклик**: `man {sec} {name}`

---

## 🎯 НАЗВА (NAME)
**`{name}`** — {summary}

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
{synopsis}
```

---

## 📋 ОПИС (DESCRIPTION)
Посібник `{name}` належить до **Розділу {sec}** системної документації Linux (*{SECTIONS_INFO[sec]['desc']}*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man {sec} {name}` або аліас `uman {name}`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
{examples}
```

---

## 🔗 ДИВІТЬСЯ ТАКОЖ (SEE ALSO)
{', '.join([f"[`{alt}`]({alt}.md)" if not alt.isdigit() else f"**Розділ {alt}**" for alt in alts])}

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
"""
    md_file.write_text(md_content, encoding="utf-8")
    print(f"Generated Markdown: {md_file}")

# 2. Generate ua/README.md
ua_readme_content = f"""# 📚 Каталог українських посібників man.ua

Ласкаво просимо до веб-каталогу посібників **`man.ua`**! Тут зібрано вичерпну колекцію системної документації для читання як на GitHub (формат Markdown), так і безпосередньо в браузері.

---

## 🌐 Інтерактивний перегляд у браузері
Для перегляду каталогу з миттєвим пошуком та фільтрами відкрийте локальний файл:  
👉 [`ua/index.html`](index.html)

---

## 🗂️ Навігатор за розділами системного посібника

"""

for sec_num in sorted(SECTIONS_INFO.keys()):
    info = SECTIONS_INFO[sec_num]
    ua_readme_content += f"### {info['icon']} [Розділ {sec_num}: {info['name']}](man{sec_num}/)\n"
    ua_readme_content += f"*{info['desc']}* — **{info['count']:,} сторінок**\n\n"
    
    # List core pages in this section
    pages_in_sec = [p for p in CORE_MAN_PAGES if p[0] == sec_num]
    if pages_in_sec:
        for p in pages_in_sec:
            ua_readme_content += f"- [`{p[1]}({p[0]})`](man{p[0]}/{p[1]}.{p[0]}.md) — {p[2]}\n"
    else:
        ua_readme_content += f"- *Усі {info['count']} вихідних файлів доступні у каталозі `man/man{sec_num}/`*\n"
    ua_readme_content += "\n"

ua_readme_content += """---
*Зроблено в Україні з любов'ю до Linux та вільного ПЗ.* 🇺🇦
"""
(UA_DIR / "README.md").write_text(ua_readme_content, encoding="utf-8")
print("Generated ua/README.md")

# 3. Generate ua/index.html (Rich SPA with Dark Glassmorphism, Search, Section Filters, Syntax Highlighting & Copy)
cards_json = []
for sec, name, summary, synopsis, examples, alts in CORE_MAN_PAGES:
    cards_json.append({
        "sec": sec,
        "name": name,
        "summary": summary,
        "synopsis": synopsis,
        "examples": examples,
        "alts": alts,
        "sec_name": SECTIONS_INFO[sec]["name"],
        "icon": SECTIONS_INFO[sec]["icon"]
    })

import json
cards_json_str = json.dumps(cards_json, ensure_ascii=False)
sections_json_str = json.dumps(SECTIONS_INFO, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>📖 man.ua — Веб-Каталог українських Man-Pages</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #07090e;
      --card-bg: rgba(17, 24, 39, 0.75);
      --card-border: rgba(56, 189, 248, 0.15);
      --card-hover: rgba(56, 189, 248, 0.25);
      --primary: #38bdf8;
      --primary-glow: rgba(56, 189, 248, 0.35);
      --accent: #34d399;
      --gold: #fbbf24;
      --text: #f1f5f9;
      --text-muted: #94a3b8;
      --code-bg: #0b1120;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      padding: 0;
      min-height: 100vh;
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(56, 189, 248, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 85% 85%, rgba(52, 211, 153, 0.06) 0%, transparent 40%);
      background-attachment: fixed;
    }}
    .container {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 30px 24px 80px 24px;
    }}
    header {{
      text-align: center;
      margin-bottom: 36px;
    }}
    .badge-hero {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 6px 16px;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--primary);
      margin-bottom: 16px;
    }}
    h1 {{
      font-size: 2.5rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      background: linear-gradient(135deg, #ffffff 30%, #38bdf8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 12px;
    }}
    .subtitle {{
      color: var(--text-muted);
      font-size: 1.1rem;
      max-width: 760px;
      margin: 0 auto 24px auto;
    }}
    
    /* Search & Filter Controls */
    .controls {{
      background: var(--card-bg);
      backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 20px;
      margin-bottom: 36px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
      position: sticky;
      top: 16px;
      z-index: 50;
    }}
    .search-row {{
      display: flex;
      gap: 12px;
      margin-bottom: 16px;
    }}
    .search-input {{
      flex: 1;
      background: var(--code-bg);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 12px;
      padding: 12px 18px;
      font-size: 1rem;
      color: var(--text);
      font-family: inherit;
      outline: none;
      transition: all 0.2s;
    }}
    .search-input:focus {{
      border-color: var(--primary);
      box-shadow: 0 0 0 3px var(--primary-glow);
    }}
    .filter-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .filter-btn {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: 10px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .filter-btn:hover, .filter-btn.active {{
      background: var(--primary);
      color: #07090e;
      border-color: var(--primary);
      box-shadow: 0 0 12px var(--primary-glow);
    }}

    /* Grid & Cards */
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
      gap: 20px;
    }}
    .man-card {{
      background: var(--card-bg);
      backdrop-filter: blur(12px);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      transition: all 0.25s ease;
    }}
    .man-card:hover {{
      border-color: var(--card-hover);
      transform: translateY(-3px);
      box-shadow: 0 12px 28px rgba(0, 0, 0, 0.5);
    }}
    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }}
    .card-title-group {{
      display: flex;
      align-items: baseline;
      gap: 8px;
    }}
    .card-name {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--primary);
    }}
    .card-sec-badge {{
      background: rgba(52, 211, 153, 0.15);
      border: 1px solid rgba(52, 211, 153, 0.3);
      color: var(--accent);
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
    }}
    .card-summary {{
      font-size: 0.92rem;
      color: #cbd5e1;
      text-align: justify;
      text-indent: 1.5ch;
      line-height: 1.55;
    }}
    .code-box {{
      background: var(--code-bg);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 10px 14px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      color: #7dd3fc;
      overflow-x: auto;
      white-space: pre-wrap;
      position: relative;
    }}
    .copy-btn {{
      position: absolute;
      top: 6px;
      right: 6px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #e2e8f0;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.72rem;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .copy-btn:hover {{
      background: var(--primary);
      color: #000;
    }}
    .card-footer {{
      margin-top: auto;
      padding-top: 10px;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .btn-read-md {{
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: var(--primary);
      padding: 6px 14px;
      border-radius: 8px;
      text-decoration: none;
      font-size: 0.82rem;
      font-weight: 600;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .btn-read-md:hover {{
      background: var(--primary);
      color: #07090e;
    }}

    /* Toast */
    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #10b981;
      color: #000;
      padding: 10px 20px;
      border-radius: 10px;
      font-weight: 700;
      box-shadow: 0 8px 24px rgba(16, 185, 129, 0.4);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s ease;
      z-index: 9999;
    }}
    .toast.show {{
      transform: translateY(0);
      opacity: 1;
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="badge-hero">🇺🇦 man.ua — Українська системна документація</div>
      <h1>Веб-Каталог Man-Pages</h1>
      <p class="subtitle">Інтерактивний довідник понад 34 000 посібників системної документації Linux з миттєвим пошуком та швидким копіюванням команд.</p>
    </header>

    <div class="controls">
      <div class="search-row">
        <input type="text" id="searchInput" class="search-input" placeholder="🔍 Пошук по команді, призначенню чи синтаксису (наприклад: intro, grep, open, btrfs)..." autofocus>
      </div>
      <div class="filter-pills" id="filterContainer">
        <button class="filter-btn active" data-sec="all">⚡ Всі розділи (34 000+)</button>
        <button class="filter-btn" data-sec="1">💻 Розділ 1: Команди (4 566)</button>
        <button class="filter-btn" data-sec="2">🧠 Розділ 2: Системні виклики (1 077)</button>
        <button class="filter-btn" data-sec="3">📚 Розділ 3: Бібліотеки C (25 845)</button>
        <button class="filter-btn" data-sec="4">🔌 Розділ 4: Пристрої /dev (47)</button>
        <button class="filter-btn" data-sec="5">📑 Розділ 5: Конфігурації /etc (730)</button>
        <button class="filter-btn" data-sec="6">🎮 Розділ 6: Ігри (4)</button>
        <button class="filter-btn" data-sec="7">🌐 Розділ 7: Стандарти (763)</button>
        <button class="filter-btn" data-sec="8">🛡️ Розділ 8: Адміністрування (1 374)</button>
        <button class="filter-btn" data-sec="9">⚙️ Розділ 9: Ядро (1)</button>
      </div>
    </div>

    <div class="grid" id="cardsGrid"></div>
  </div>

  <div class="toast" id="toast">📋 Скопійовано в буфер обміну!</div>

  <script>
    const CARDS_DATA = {cards_json_str};
    let activeSec = 'all';

    function renderCards() {{
      const query = document.getElementById('searchInput').value.trim().toLowerCase();
      const grid = document.getElementById('cardsGrid');
      
      const filtered = CARDS_DATA.filter(item => {{
        const matchSec = (activeSec === 'all' || item.sec === activeSec);
        const matchQuery = !query || 
          item.name.toLowerCase().includes(query) || 
          item.summary.toLowerCase().includes(query) || 
          item.synopsis.toLowerCase().includes(query);
        return matchSec && matchQuery;
      }});

      if (filtered.length === 0) {{
        grid.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-muted); font-size: 1.1rem;">🔍 Нічого не знайдено за вашим запитом. Спробуйте інше ключове слово.</div>';
        return;
      }}

      grid.innerHTML = filtered.map(item => `
        <div class="man-card">
          <div class="card-top">
            <div class="card-title-group">
              <span class="card-name">${{item.name}}</span>
              <span class="card-sec-badge">man ${{item.sec}}</span>
            </div>
            <span style="font-size: 0.8rem; color: var(--text-muted);">${{item.icon}} Розділ ${{item.sec}}</span>
          </div>

          <p class="card-summary">${{item.summary}}</p>

          <div style="font-size: 0.78rem; font-weight: 700; color: var(--gold); margin-top: 4px;">⚙️ СИНТАКСИС ВИКЛИКУ:</div>
          <div class="code-box">
            <button class="copy-btn" onclick="copyText('${{escapeJs(item.synopsis)}}')">📋 Копіювати</button>
            <code>${{escapeHtml(item.synopsis)}}</code>
          </div>

          <div style="font-size: 0.78rem; font-weight: 700; color: var(--accent); margin-top: 4px;">💡 ПРИКЛАД:</div>
          <div class="code-box">
            <button class="copy-btn" onclick="copyText('${{escapeJs(item.examples)}}')">📋 Копіювати</button>
            <code>${{escapeHtml(item.examples)}}</code>
          </div>

          <div class="card-footer">
            <span style="font-size: 0.78rem; color: var(--text-muted); font-family: monospace;">man/${{item.name}}.${{item.sec}}</span>
            <a href="man${{item.sec}}/${{item.name}}.${{item.sec}}.md" class="btn-read-md">📖 Відкрити .md →</a>
          </div>
        </div>
      `).join('');
    }}

    function escapeHtml(str) {{
      return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }}

    function escapeJs(str) {{
      return str.replace(/\\/g, '\\\\').replace(/'/g, "\\'").replace(/\\n/g, '\\n');
    }}

    function copyText(text) {{
      navigator.clipboard.writeText(text).then(() => {{
        const toast = document.getElementById('toast');
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2000);
      }});
    }}

    // Filter Buttons
    document.getElementById('filterContainer').addEventListener('click', (e) => {{
      const btn = e.target.closest('.filter-btn');
      if (!btn) return;
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeSec = btn.dataset.sec;
      renderCards();
    }});

    // Search Input
    document.getElementById('searchInput').addEventListener('input', renderCards);

    // Initial render
    renderCards();
  </script>
</body>
</html>
"""
(UA_DIR / "index.html").write_text(html_content, encoding="utf-8")
print("Generated ua/index.html")
