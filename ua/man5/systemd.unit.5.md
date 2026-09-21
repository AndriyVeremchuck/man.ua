# 📖 systemd.unit(5) — Українська системна документація

> **Розділ 5**: Формати конфігураційних файлів (/etc)  
> **Пакет**: `systemd`  
> **Оригінальний виклик**: `man 5 systemd.unit`

---

## 🎯 НАЗВА (NAME)
**`systemd.unit`** — Формат конфігураційних unit-файлів сервісів systemd (.service, .socket, .timer)

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
[Unit]
Description=...
[Service]
ExecStart=...
```

---

## 📋 ОПИС (DESCRIPTION)
Посібник `systemd.unit` належить до **Розділу 5** системної документації Linux (*Синтаксис конфігураційних файлів (/etc/passwd, fstab, crontab, systemd)*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 5 systemd.unit` або аліас `uman systemd.unit`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
[Unit]
Description=My Service
[Service]
ExecStart=/usr/bin/python3 /app.py
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
