# 📖 clone(2) — Українська системна документація

> **Розділ 2**: Системні виклики ядра Linux  
> **Оригінальний виклик**: `man 2 clone`

---

## 🎯 НАЗВА (NAME)
**`clone`** — Створення дочірнього процесу або потоку з налаштуванням просторів імен

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
int clone(int (*fn)(void *), void *stack, int flags, void *arg, ...);
```

---

## 📋 ОПИС (DESCRIPTION)
Посібник `clone` належить до **Розділу 2** системної документації Linux (*Прямі системні виклики між простором користувача та ядром (syscalls)*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 2 clone` або аліас `uman clone`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
clone(child_fn, stack_top, CLONE_VM | CLONE_FS | SIGCHLD, NULL);
```

---

## 🔗 ДИВІТЬСЯ ТАКОЖ (SEE ALSO)
**Розділ 2**, [`fork`](fork.md), [`unshare`](unshare.md), [`namespaces`](namespaces.md)

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
