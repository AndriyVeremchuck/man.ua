# 📖 asciidoctor(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `asciidoctor`  
> **Оригінальний виклик**: `man 1 asciidoctor`

---

## 🎯 НАЗВА (NAME)
**`asciidoctor`** — Швидкий та елегантний процесор розмітки AsciiDoc: перетворення технічної документації та книг у сучасний HTML5, DocBook, PDF та EPUB3.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
asciidoctor [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`-b <html5/docbook5/pdf/epub3>, -d <article/book>, -a toc, -o <вихідний_файл>`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `asciidoctor` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 asciidoctor` або аліас `uman asciidoctor`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ asciidoctor -b html5 -a toc documentation.adoc  # Генерація красивої HTML5 документації з бічним змістом
$ asciidoctor -b docbook5 manual.adoc  # Трансляція тексту AsciiDoc у стандарт DocBook 5
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
