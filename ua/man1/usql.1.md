# 📖 usql(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `usql`  
> **Оригінальний виклик**: `man 1 usql`

---

## 🎯 НАЗВА (NAME)
**`usql`** — Універсальний командний SQL-клієнт на Go для підключення до PostgreSQL, MySQL, SQLite, Oracle, SQL Server, ClickHouse та Redis.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
usql [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`<DSN_рядок_підключення>, -c "<SQL_запит>", -f <файл.sql>, --json`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `usql` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 usql` або аліас `uman usql`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ usql postgres://user:pass@localhost/mydb  # Інтерактивне підключення до бази даних PostgreSQL
$ usql sqlite://database.db -c "SELECT * FROM users LIMIT 10;"  # Швидке виконання SQL запиту до бази SQLite
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
