# 📖 execve(2) — Українська системна документація

> **Розділ 2**: Системні виклики ядра Linux  
> **Пакет**: `system`  
> **Оригінальний виклик**: `man 2 execve`

---

## 🎯 НАЗВА (NAME)
**`execve`** — Запуск виконуваного бінарного файлу або скрипта з передачею аргументів та середовища

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
int execve(const char *pathname, char *const _Nullable argv[], char *const _Nullable envp[]);
```

---

## 📋 ОПИС (DESCRIPTION)
Посібник `execve` належить до **Розділу 2** системної документації Linux (*Прямі системні виклики між простором користувача та ядром (syscalls)*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 2 execve` або аліас `uman execve`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
execve("/bin/ls", argv, envp);
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
