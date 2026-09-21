# 📖 wl_display_connect(3) — Українська системна документація

> **Розділ 3**: Бібліотечні виклики C / libc / Wayland API  
> **Пакет**: `wayland`  
> **Оригінальний виклик**: `man 3 wl_display_connect`

---

## 🎯 НАЗВА (NAME)
**`wl_display_connect`** — Підключення клієнта до Wayland-композитора через UNIX-сокет

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
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
