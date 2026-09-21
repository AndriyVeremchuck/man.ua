# 📖 libreoffice(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `libreoffice-fresh`  
> **Оригінальний виклик**: `man 1 libreoffice`

---

## 🎯 НАЗВА (NAME)
**`libreoffice`** — Універсальний пакетний конвертер офісних форматів у режимі headless: бездоганне перетворення ODT, DOCX, XLSX, PPTX, RTF у PDF або HTML.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
libreoffice [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`--headless (робота без GUI), --convert-to <pdf/html/docx/odt>, --outdir <папка_виводу>`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `libreoffice` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 libreoffice` або аліас `uman libreoffice`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ libreoffice --headless --convert-to pdf document.docx  # Пряма консольна конвертація документа Word DOCX у PDF
$ libreoffice --headless --convert-to pdf --outdir ./pdf_out/ *.odt  # Пакетне перетворення всіх документів ODT у формат PDF
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
