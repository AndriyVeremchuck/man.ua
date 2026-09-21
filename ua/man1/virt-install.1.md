# 📖 virt-install(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `virt-install`  
> **Оригінальний виклик**: `man 1 virt-install`

---

## 🎯 НАЗВА (NAME)
**`virt-install`** — Інструмент створення та автоматизованого розгортання нових віртуальних машин KVM із конфігурацією RAM, vCPU, дисків та ISO-образів.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
virt-install [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`--name <назва>, --memory <МБ>, --vcpus <кількість>, --disk <шлях>, --cdrom <iso>, --os-variant <os>`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `virt-install` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 virt-install` або аліас `uman virt-install`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ virt-install --name ubuntu-test --memory 4096 --vcpus 4 --disk size=30 --cdrom ubuntu.iso --os-variant ubuntu22.04  # Створення нової VM Ubuntu з 4 ядрами та 4 ГБ RAM
$ virt-install --osinfo list  # Перегляд підтримуваних профілів операційних систем
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
