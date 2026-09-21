#!/usr/bin/env bash
# ==============================================================================
# 📖 man.ua — Автоматичний скрипт встановлення українських man-сторінок
# ==============================================================================

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}======================================================${NC}"
echo -e "${GREEN}📖 man.ua: Встановлення українських системних посібників${NC}"
echo -e "${BLUE}======================================================${NC}"

# Перевірка прав root
if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}❌ Помилка: Запустіть цей скрипт із правами root або sudo:${NC}"
    echo -e "   ${YELLOW}sudo ./install.sh${NC}"
    exit 1
fi

DEST_DIR="/usr/share/man/uk"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "\n${YELLOW}1/4. Створення цільової директорії ${DEST_DIR}...${NC}"
mkdir -p "${DEST_DIR}"

echo -e "${YELLOW}2/4. Копіювання розділів man-сторінок (man1 - man9)...${NC}"
for sec in 1 2 3 4 5 6 7 8 9; do
    if [ -d "${SCRIPT_DIR}/man${sec}" ]; then
        mkdir -p "${DEST_DIR}/man${sec}"
        cp -r "${SCRIPT_DIR}/man${sec}/"* "${DEST_DIR}/man${sec}/" 2>/dev/null || true
        count=$(find "${DEST_DIR}/man${sec}" -type f | wc -l)
        echo -e "   ✓ ${GREEN}man${sec}${NC}: скопійовано (${count} сторінок)"
    fi
done

# Встановлення правильних прав доступу
chmod -R 755 "${DEST_DIR}"
find "${DEST_DIR}" -type f -exec chmod 644 {} +

echo -e "\n${YELLOW}3/4. Перевірка локалі uk_UA.UTF-8...${NC}"
if command -v locale-gen &>/dev/null; then
    if ! locale -a | grep -qi "uk_UA.utf8"; then
        echo -e "   ℹ️ Генерація локалі uk_UA.UTF-8..."
        if [ -f /etc/locale.gen ]; then
            sed -i 's/^# *uk_UA.UTF-8 UTF-8/uk_UA.UTF-8 UTF-8/' /etc/locale.gen
            locale-gen
        else
            locale-gen uk_UA.UTF-8 2>/dev/null || true
        fi
    else
        echo -e "   ✓ Локаль ${GREEN}uk_UA.UTF-8${NC} присутня в системі"
    fi
fi

echo -e "\n${YELLOW}4/4. Оновлення індексу бази даних посібників (mandb)...${NC}"
if command -v mandb &>/dev/null; then
    mandb -q 2>/dev/null || mandb || true
    echo -e "   ✓ Індекс ${GREEN}mandb${NC} успішно оновлено"
fi

echo -e "\n${BLUE}======================================================${NC}"
echo -e "${GREEN}🎉 Встановлення успішно завершено!${NC}"
echo -e "${BLUE}======================================================${NC}"
echo -e "💡 Тепер ви можете відкривати посібники командою:"
echo -e "   ${YELLOW}man intro${NC}"
echo -e "   ${YELLOW}man man${NC}"
echo -e "   ${YELLOW}man 1 ls${NC}"
echo -e "   ${YELLOW}man -L uk <команда>${NC} (якщо системна мова англійська)\n"
