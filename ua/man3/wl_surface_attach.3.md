# 📖 wl_surface_attach(3) — Українська системна документація

> **Розділ 3**: Бібліотечні виклики C / libc / Wayland API  
> **Пакет**: `wayland`  
> **Оригінальний виклик**: `man 3 wl_surface_attach`

---

## 🎯 НАЗВА (NAME)
**`wl_surface_attach`** — Прикріплення графічного буфера wl_buffer до поверхні wl_surface

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
void wl_surface_attach(struct wl_surface *wl_surface, struct wl_buffer *buffer, int32_t x, int32_t y);
```

---

## 📋 ОПИС (DESCRIPTION)
Посібник `wl_surface_attach` належить до **Розділу 3** системної документації Linux (*Функції glibc, posix, wayland та системних C-бібліотек*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 3 wl_surface_attach` або аліас `uman wl_surface_attach`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
wl_surface_attach(surface, buffer, 0, 0);
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
