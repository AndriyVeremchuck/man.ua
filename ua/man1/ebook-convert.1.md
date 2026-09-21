# 📖 ebook-convert(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `calibre`  
> **Оригінальний виклик**: `man 1 ebook-convert`

---

## 🎯 НАЗВА (NAME)
**`ebook-convert`** — Еталонний швейцарський ніж електронних книг від Calibre: конвертація між EPUB, MOBI, AZW3, FB2, PDF, RTF, DOCX, TXT з оптимізацією верстки.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
ebook-convert [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`--subset-embedded-fonts, --base-font-size=<pt>, --margin-top=<pt>, --embed-all-fonts`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `ebook-convert` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 ebook-convert` або аліас `uman ebook-convert`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ ebook-convert book.fb2 book.epub  # Конвертація книги з формату FB2 у сучасний стандарт EPUB
$ ebook-convert book.epub book.pdf --paper-size a4 --pdf-default-font-size 12  # Генерація зручного PDF для друку з книги EPUB
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
