# 📖 reflector(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `reflector`  
> **Оригінальний виклик**: `man 1 reflector`

---

## 🎯 НАЗВА (NAME)
**`reflector`** — Python-скрипт для автоматичного отримання останнього списку дзеркал Arch Linux, їх фільтрації за швидкістю, країною та збереження у mirrorlist.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
reflector [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`--country <країни> (фільтр за країнами), --latest <N> (кількість останніх), --sort <rate/score/delay>, --save <шлях>`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `reflector` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 reflector` або аліас `uman reflector`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ sudo reflector --country Ukraine,Germany,Poland --latest 10 --sort rate --save /etc/pacman.d/mirrorlist  # Вибір 10 найшвидших сусідніх дзеркал
$ reflector --score 5 --sort rate  # Тестування та виведення рейтингу дзеркал у консоль
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
