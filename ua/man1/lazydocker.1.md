# 📖 lazydocker(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `lazydocker`  
> **Оригінальний виклик**: `man 1 lazydocker`

---

## 🎯 НАЗВА (NAME)
**`lazydocker`** — Простий та потужний TUI для Docker та Docker Compose на Go: перегляд логів, використання CPU/RAM контейнерами, зупинка/перезапуск та очищення томиків.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
lazydocker [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`-f <docker-compose.yml>, --compose-files, --log, -e (debug)`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `lazydocker` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 lazydocker` або аліас `uman lazydocker`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ lazydocker  # Інтерактивна TUI-панель моніторингу та керування контейнерами Docker
$ lazydocker -f docker-compose.prod.yml  # Керування контейнерами конкретного Compose файлу
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
