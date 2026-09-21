# 📖 nvidia-smi(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `nvidia-utils`  
> **Оригінальний виклик**: `man 1 nvidia-smi`

---

## 🎯 НАЗВА (NAME)
**`nvidia-smi`** — NVIDIA System Management Interface — офіційна утиліта моніторингу та керування відеокартами NVIDIA GeForce / RTX (VRAM, температура, TDP, процеси CUDA).

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
nvidia-smi [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`-l <сек> (періодичне оновлення), --query-gpu=... (вибірка метрик), --format=csv (вивід у CSV), -i <id> (вибір конкретної GPU), -pm 1 (увімкнення Persistence Mode)`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `nvidia-smi` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 nvidia-smi` або аліас `uman nvidia-smi`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ nvidia-smi  # Огляд стану RTX 3060: температура, споживання енергії, зайнята відеопам'ять
$ nvidia-smi --query-gpu=temperature.gpu,utilization.gpu,memory.used --format=csv -l 1  # Моніторинг температури та завантаження GPU щосекунди
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
