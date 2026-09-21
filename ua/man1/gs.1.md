# 📖 gs(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `ghostscript`  
> **Оригінальний виклик**: `man 1 gs`

---

## 🎯 НАЗВА (NAME)
**`gs`** — Потужний галузевий рушій інтерпретації PostScript та PDF: радикальне стиснення розміру PDF, оптимізація колірних профілів CMYK/RGB та перетворення форматів.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
gs [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`-sDEVICE=pdfwrite, -dPDFSETTINGS=/screen|/ebook|/printer, -dCompatibilityLevel=1.4, -dNOPAUSE, -dBATCH`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `gs` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 gs` або аліас `uman gs`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=small.pdf large.pdf  # Зменшення розміру PDF документа для зручного надсилання поштою
$ gs -sDEVICE=pdfwrite -dPDFSETTINGS=/screen -dNOPAUSE -dBATCH -sOutputFile=compressed.pdf input.pdf  # Максимальне стиснення графіки у PDF (72 DPI)
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
