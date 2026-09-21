# 📖 vboxmanage(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `virtualbox-cli`  
> **Оригінальний виклик**: `man 1 vboxmanage`

---

## 🎯 НАЗВА (NAME)
**`vboxmanage`** — Повний інтерфейс командного рядка для керування віртуальними машинами, знімками станів та адаптерами VirtualBox.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
vboxmanage [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`list vms (список VM), startvm <ім'я> [--type headless], controlvm <ім'я> poweroff, snapshot <ім'я> take <назва>`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `vboxmanage` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 vboxmanage` або аліас `uman vboxmanage`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ VBoxManage list vms  # Список усіх зареєстрованих віртуальних машин VirtualBox
$ VBoxManage startvm "UbuntuServer" --type headless  # Запуск віртуальної машини у фоні без графічного вікна
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
