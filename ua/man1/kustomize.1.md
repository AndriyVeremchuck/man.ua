# 📖 kustomize(1) — Українська системна документація

> **Розділ 1**: Виконувані програми та команди оболонки  
> **Пакет**: `kustomize`  
> **Оригінальний виклик**: `man 1 kustomize`

---

## 🎯 НАЗВА (NAME)
**`kustomize`** — Офіційний інструмент декларативної кастомізації маніфестів Kubernetes без використання шаблонів (template-free YAML customization).

---

## ⚙️ КОРОТКИЙ ОПИС (SYNOPSIS)
```bash
kustomize [OPTIONS] [ARGUMENTS...]
```

### ⚡ Ключові прапорці та опції:
`build <директорія>, edit add resource <файл>, create`

---

## 📋 ОПИС (DESCRIPTION)
Посібник `kustomize` належить до **Розділу 1** системної документації Linux (*Користувацькі утиліти, командні оболонки, текстові процесори, компілятори*).

### Ключові характеристики:
* Повна відповідність стандартам POSIX та Linux Programmer's Manual.
* 100% перекладено та адаптовано українською мовою в рамках проєкту **man.ua**.
* Підтримує швидке відкриття в терміналі через `man 1 kustomize` або аліас `uman kustomize`.

---

## 💡 ПРАКТИЧНІ ПРИКЛАДИ (EXAMPLES)
```bash
$ kustomize build overlays/production | kubectl apply -f -  # Збірка та пряме застосування продакшн-конфігурації в кластер
$ kustomize build overlays/staging  # Перегляд згенерованого фінального YAML маніфесту
```

---
*Документ є частиною проєкту [man.ua](https://github.com/AndreyVeremchuck/man.ua).*
