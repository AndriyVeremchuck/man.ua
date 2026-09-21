# 📖 wl_display_connect(3) — Українська системна документація

> **Розділ 3**: Бібліотечні виклики C / libc / Wayland API  
> **Оригінальний виклик**: `man 3 wl_display_connect`

---

## 🎯 НАЗВА (NAME)
**`wl_display_connect`** — Підключення клієнтського додатку до Wayland-композитора

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
struct wl_display *wl_display_connect(const char *name);
```

---

## 📋 ОПИС (DESCRIPTION)
Посібник `wl_display_connect` належить до **Розділу 3** системної документації Linux (*Функції glibc, posix, wayland та системних C-бібліотек*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 3 wl_display_connect` або аліас `uman wl_display_connect`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
struct wl_display *dpy = wl_display_connect(NULL);
```

---

## 🔗 ДИВІТЬСЯ ТАКОЖ (SEE ALSO)
**Розділ 3**, [`wl_display_disconnect`](wl_display_disconnect.md), [`wayland`](wayland.md)

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
