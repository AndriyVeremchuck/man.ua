PREFIX ?= /usr/share/man/uk
MAN_SRC ?= man

.PHONY: all install uninstall help

all: help

help:
	@echo "📖 man.ua — Команди для встановлення:"
	@echo "  sudo make install    - Встановити всі розділи з man/man1-man9 в $(PREFIX)"
	@echo "  sudo make uninstall  - Видалити встановлені сторінки з $(PREFIX)"

install:
	@echo "Встановлення man-сторінок у $(PREFIX)..."
	@mkdir -p $(PREFIX)
	@for sec in 1 2 3 4 5 6 7 8 9; do \
		if [ -d "$(MAN_SRC)/man$$sec" ]; then \
			mkdir -p $(PREFIX)/man$$sec; \
			cp -r $(MAN_SRC)/man$$sec/* $(PREFIX)/man$$sec/ 2>/dev/null || true; \
		fi \
	done
	@chmod -R 755 $(PREFIX)
	@find $(PREFIX) -type f -exec chmod 644 {} +
	@if command -v mandb >/dev/null 2>&1; then mandb -q 2>/dev/null || mandb || true; fi
	@echo "✓ Встановлення завершено!"

uninstall:
	@echo "Видалення $(PREFIX)..."
	@rm -rf $(PREFIX)
	@if command -v mandb >/dev/null 2>&1; then mandb -q 2>/dev/null || mandb || true; fi
	@echo "✓ Видалено!"
