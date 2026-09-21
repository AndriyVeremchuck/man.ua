# 📖 null(4) — Українська системна документація

> **Розділ 4**: Спеціальні файли та пристрої (/dev)  
> **Оригінальний виклик**: `man 4 null`

---

## 🎯 НАЗВА (NAME)
**`null`** — Нульовий пристрій скидання даних (/dev/null) та генератор нулів (/dev/zero)

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
/dev/null, /dev/zero
```

---

## 📋 ОПИС (DESCRIPTION)
Посібник `null` належить до **Розділу 4** системної документації Linux (*Драйвери пристроїв, псевдо-пристрої (/dev/null, /dev/random, /dev/tty)*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 4 null` або аліас `uman null`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ command > /dev/null 2>&1
$ dd if=/dev/zero of=test.img bs=1M count=10
```

---

## 🔗 ДИВІТЬСЯ ТАКОЖ (SEE ALSO)
**Розділ 4**, [`zero`](zero.md), [`random`](random.md), [`urandom`](urandom.md)

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
