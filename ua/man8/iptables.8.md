# 📖 iptables(8) — Українська системна документація

> **Розділ 8**: Команди системного адміністрування (Root)  
> **Пакет**: `iptables`  
> **Оригінальний виклик**: `man 8 iptables`

---

## 🎯 НАЗВА (NAME)
**`iptables`** — Адміністрування міжмережевого екрана IPv4 та фільтрація пакетів

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
iptables [-t table] {-A|-D|-I} chain rule-specification
```

---

## 📋 ОПИС (DESCRIPTION)
Посібник `iptables` належить до **Розділу 8** системної документації Linux (*Утиліти керування службами, дисками, демонами, безпекою (systemctl, btrfs)*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 8 iptables` або аліас `uman iptables`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ sudo iptables -L -n -v
$ sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
