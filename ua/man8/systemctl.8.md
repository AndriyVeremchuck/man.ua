# 📖 systemctl(8) — Українська системна документація

> **Розділ 8**: Команди системного адміністрування (Root)  
> **Пакет**: `systemd`  
> **Оригінальний виклик**: `man 8 systemctl`

---

## 🎯 НАЗВА (NAME)
**`systemctl`** — Центральний інструмент керування системними службами, демонами, сокетами та таймерами systemd.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
systemctl [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`status <юніт>, start/stop, enable/disable --now, list-units --type=service, --user (користувацькі)`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `systemctl` належить до **Розділу 8** системної документації Linux (*Утиліти керування службами, дисками, демонами, безпекою (systemctl, btrfs)*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 8 systemctl` або аліас `uman systemctl`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ systemctl status NetworkManager.service  # Перевірити статус мережевої служби
$ systemctl list-units --type=service --state=running  # Список усіх активних працюючих служб
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
