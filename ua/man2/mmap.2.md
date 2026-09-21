# 📖 mmap(2) — Українська системна документація

> **Розділ 2**: Системні виклики ядра Linux  
> **Пакет**: `system`  
> **Оригінальний виклик**: `man 2 mmap`

---

## 🎯 НАЗВА (NAME)
**`mmap`** — Відображення файлів або пристроїв у віртуальну пам'ять процесу

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
void *mmap(void addr[.length], size_t length, int prot, int flags, int fd, off_t offset);
```

---

## 📋 ОПИС (DESCRIPTION)
Посібник `mmap` належить до **Розділу 2** системної документації Linux (*Прямі системні виклики між простором користувача та ядром (syscalls)*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 2 mmap` або аліас `uman mmap`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
void *ptr = mmap(NULL, size, PROT_READ, MAP_PRIVATE, fd, 0);
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
