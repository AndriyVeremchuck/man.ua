# 📖 pthread_create(3) — Українська системна документація

> **Розділ 3**: Бібліотечні виклики C / libc / Wayland API  
> **Пакет**: `pthreads`  
> **Оригінальний виклик**: `man 3 pthread_create`

---

## 🎯 НАЗВА (NAME)
**`pthread_create`** — Створення нового потоку виконання (POSIX thread)

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
int pthread_create(pthread_t *thread, const pthread_attr_t *attr, void *(*start_routine) (void *), void *arg);
```

---

## 📋 ОПИС (DESCRIPTION)
Посібник `pthread_create` належить до **Розділу 3** системної документації Linux (*Функції glibc, posix, wayland та системних C-бібліотек*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 3 pthread_create` або аліас `uman pthread_create`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
pthread_create(&tid, NULL, worker_fn, NULL);
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
