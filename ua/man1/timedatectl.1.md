# 📖 timedatectl(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `systemd`  
> **Оригінальний виклик**: `man 1 timedatectl`

---

## 🎯 НАЗВА (NAME)
**`timedatectl`** — Керування системним часом, датою, часовим поясом (timezone) та статусом автоматичної мережевої синхронізації часу NTP (systemd-timesyncd).

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
timedatectl [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`status (поточний час та статус NTP), set-timezone <зона>, list-timezones, set-ntp true/false`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `timedatectl` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 timedatectl` або аліас `uman timedatectl`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ timedatectl status  # Перевірка локального часу, часу RTC та статусу синхронізації NTP
$ sudo timedatectl set-timezone Europe/Kyiv  # Встановлення часового поясу Києва
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
