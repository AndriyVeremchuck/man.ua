# 📖 cachyos-rate-mirrors(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `cachyos-rate-mirrors`  
> **Оригінальний виклик**: `man 1 cachyos-rate-mirrors`

---

## 🎯 НАЗВА (NAME)
**`cachyos-rate-mirrors`** — Фірмовий бенчмаркер дзеркал CachyOS для тестування швидкості відгуку та автоматичного сортування найшвидших серверів репозиторіїв.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
cachyos-rate-mirrors [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`--save <файл> (збереження mirrorlist), --top <N> (кількість найшвидших дзеркал)`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `cachyos-rate-mirrors` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 cachyos-rate-mirrors` або аліас `uman cachyos-rate-mirrors`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ sudo cachyos-rate-mirrors  # Тестування та оновлення списку найшвидших дзеркал CachyOS
$ rate-mirrors arch | sudo tee /etc/pacman.d/mirrorlist  # Оновлення дзеркал Arch Linux на основі найменшого пінг-відгуку
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
