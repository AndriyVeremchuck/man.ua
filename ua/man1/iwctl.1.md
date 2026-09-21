# 📖 iwctl(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `iwd`  
> **Оригінальний виклик**: `man 1 iwctl`

---

## 🎯 НАЗВА (NAME)
**`iwctl`** — Інтерактивна командна оболонка швидкого демона iNet Wireless Daemon (iwd) для підключення до сучасних мереж Wi-Fi WPA2/WPA3 Personal та Enterprise.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
iwctl [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`station <wlan> scan, station <wlan> get-networks, station <wlan> connect <SSID>, device list`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `iwctl` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 iwctl` або аліас `uman iwctl`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ iwctl device list  # Список виявлених Wi-Fi адаптерів під керуванням iwd
$ iwctl station wlan0 get-networks  # Перегляд доступних бездротових мереж та рівня сигналу
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
