#!/usr/bin/env bash
# ==============================================================================
# 📖 man.ua — Скрипт видалення встановлених українських man-сторінок
# ==============================================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}❌ Запустіть скрипт із правами root або sudo:${NC}"
    echo -e "   ${YELLOW}sudo ./uninstall.sh${NC}"
    exit 1
fi

DEST_DIR="/usr/share/man/uk"

if [ -d "${DEST_DIR}" ]; then
    echo -e "${YELLOW}Видалення каталогу ${DEST_DIR}...${NC}"
    rm -rf "${DEST_DIR}"
    echo -e "${GREEN}✓ Каталог ${DEST_DIR} видалено.${NC}"
fi

echo -e "${YELLOW}Оновлення індексу mandb...${NC}"
if command -v mandb &>/dev/null; then
    mandb -q 2>/dev/null || mandb || true
fi

echo -e "${GREEN}🎉 Видалення завершено.${NC}"
