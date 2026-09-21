# 📖 ps2pdf(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `ghostscript`  
> **Оригінальний виклик**: `man 1 ps2pdf`

---

## 🎯 НАЗВА (NAME)
**`ps2pdf`** — Пряме перетворення файлів PostScript (.ps, .eps) у стандартний формат PDF за допомогою рушія Ghostscript.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
ps2pdf [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`-dPDFSETTINGS=/printer, -dAutoRotatePages=/None, <вхідний.ps> [вихідний.pdf]`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `ps2pdf` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 ps2pdf` або аліас `uman ps2pdf`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ ps2pdf document.ps document.pdf  # Конвертація файлу PostScript у PDF
$ ps2pdf -dPDFSETTINGS=/prepress diagram.eps diagram.pdf  # Високоякісна конвертація векторного EPS для типографії
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
