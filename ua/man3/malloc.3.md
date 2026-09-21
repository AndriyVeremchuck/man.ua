# 📖 malloc(3) — Українська системна документація

> **Розділ 3**: Бібліотечні виклики C / libc / Wayland API  
> **Оригінальний виклик**: `man 3 malloc`

---

## 🎯 НАЗВА (NAME)
**`malloc`** — Динамічне виділення блоку пам'яті заданого розміру у купі (heap)

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
void *malloc(size_t size);
```

---

## 📋 ОПИС (DESCRIPTION)
Посібник `malloc` належить до **Розділу 3** системної документації Linux (*Функції glibc, posix, wayland та системних C-бібліотек*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 3 malloc` або аліас `uman malloc`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
char *buf = (char *)malloc(1024);
if (!buf) { /* помилка */ }
free(buf);
```

---

## 🔗 ДИВІТЬСЯ ТАКОЖ (SEE ALSO)
**Розділ 3**, [`free`](free.md), [`calloc`](calloc.md), [`realloc`](realloc.md)

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
