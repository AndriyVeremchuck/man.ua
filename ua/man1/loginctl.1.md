# 📖 loginctl(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `systemd`  
> **Оригінальний виклик**: `man 1 loginctl`

---

## 🎯 НАЗВА (NAME)
**`loginctl`** — Керування сесіями користувачів, робочими місцями (seats) та станом демона systemd-logind у графічному середовищі KDE Plasma.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
loginctl [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`list-sessions (активні сесії), session-status <id>, list-users, terminate-session <id> (закрити сесію), lock-session`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `loginctl` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 loginctl` або аліас `uman loginctl`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ loginctl list-sessions  # Список відкритих графічних та TTY сесій користувачів
$ loginctl session-status  # Перегляд типу сесії (Wayland або X11) та пов'язаних процесів
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
