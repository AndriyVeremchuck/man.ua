# 📖 cryptsetup(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `cryptsetup`  
> **Оригінальний виклик**: `man 1 cryptsetup`

---

## 🎯 НАЗВА (NAME)
**`cryptsetup`** — Керування криптографічно захищеними розділами дисків стандарту LUKS (Linux Unified Key Setup) та модулем ядра dm-crypt.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
cryptsetup [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`luksFormat (форматування розділу у LUKS), open / luksOpen (розблокування розділу), close / luksClose (блокування), luksDump (перегляд метаданих)`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `cryptsetup` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 cryptsetup` або аліас `uman cryptsetup`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ sudo cryptsetup open /dev/nvme0n1p3 cryptroot  # Розблокування зашифрованого кореневого розділу LUKS
$ sudo cryptsetup luksDump /dev/nvme0n1p3  # Перегляд слотів ключів, алгоритму шифрування та параметрів тома
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
