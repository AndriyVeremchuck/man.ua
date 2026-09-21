# 📖 x86_energy_perf_policy(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `linux-tools`  
> **Оригінальний виклик**: `man 1 x86_energy_perf_policy`

---

## 🎯 НАЗВА (NAME)
**`x86_energy_perf_policy`** — Утиліта налаштування внутрішньої енергетичної політики процесорів x86 (Energy Performance Preference): performance, balance-performance, power.

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
x86_energy_perf_policy [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`-r (читання поточних значень), performance, balance-performance, balance-power, power`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `x86_energy_perf_policy` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 x86_energy_perf_policy` або аліас `uman x86_energy_perf_policy`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ sudo x86_energy_perf_policy -r  # Перегляд поточної апаратної політики енергобалансу процесора
$ sudo x86_energy_perf_policy performance  # Встановлення найвищого пріоритету продуктивності для всіх ядер
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
