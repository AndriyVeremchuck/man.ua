# 📖 pdftops(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `poppler`  
> **Оригінальний виклик**: `man 1 pdftops`

---

## 🎯 НАЗВА (NAME)
**`pdftops`** — Високоточне перетворення документів PDF у векторний формат PostScript Level 2/3 або Encapsulated PostScript (EPS).

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
pdftops [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`-level3 (PostScript Level 3), -eps (створити Encapsulated PostScript), -f <перша>, -l <остання>`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `pdftops` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 pdftops` або аліас `uman pdftops`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ pdftops -level3 document.pdf output.ps  # Конвертація PDF у чистий PostScript Level 3
$ pdftops -eps -f 1 -l 1 diagram.pdf diagram.eps  # Створення векторного EPS файлу з першої сторінки PDF
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
