#!/usr/bin/env python3
"""
Generator for crisp terminal screenshots of man pages (man man, man intro)
"""
import os
from PIL import Image, ImageDraw, ImageFont

def render_terminal_screenshot(output_path, title, prompt_cmd, lines_data, status_bar=""):
    width = 1200
    line_height = 28
    font_size = 18
    title_font_size = 16
    padding_x = 36
    padding_top = 70
    padding_bottom = 50
    
    total_lines = len(lines_data) + 2  # prompt + spacer + lines
    height = padding_top + (total_lines * line_height) + padding_bottom
    
    # Base background: Dark cyberpunk / modern sleek terminal (#0b0f19)
    img = Image.new('RGBA', (width, height), (11, 15, 25, 255))
    draw = ImageDraw.Draw(img)
    
    font_reg_path = "/usr/share/fonts/TTF/JetBrainsMono-Regular.ttf"
    font_bold_path = "/usr/share/fonts/TTF/JetBrainsMono-Bold.ttf"
    
    try:
        font_regular = ImageFont.truetype(font_reg_path, font_size)
        font_bold = ImageFont.truetype(font_bold_path, font_size)
        font_title = ImageFont.truetype(font_bold_path, title_font_size)
        font_status = ImageFont.truetype(font_bold_path, 15)
    except Exception:
        font_regular = ImageFont.load_default()
        font_bold = ImageFont.load_default()
        font_title = ImageFont.load_default()
        font_status = ImageFont.load_default()
        
    # Draw Window Header Bar (#161e2e)
    header_height = 46
    draw.rectangle([(0, 0), (width, header_height)], fill=(22, 30, 46, 255))
    draw.line([(0, header_height), (width, header_height)], fill=(38, 50, 75, 255), width=1)
    
    # macOS / Modern window buttons
    btn_y = 23
    draw.ellipse([(22, btn_y - 6), (34, btn_y + 6)], fill=(239, 68, 68, 255))      # Close Red
    draw.ellipse([(42, btn_y - 6), (54, btn_y + 6)], fill=(245, 158, 11, 255))     # Min Yellow
    draw.ellipse([(62, btn_y - 6), (74, btn_y + 6)], fill=(16, 185, 129, 255))     # Max Green
    
    # Window Title
    draw.text((width // 2, 23), title, fill=(156, 163, 175, 255), font=font_title, anchor="mm")
    
    # Draw Terminal Prompt
    cur_y = padding_top
    # Prompt prefix: green user@host, blue path
    draw.text((padding_x, cur_y), "dusha@cachyos-pc", fill=(52, 211, 153, 255), font=font_bold)
    w1 = font_bold.getlength("dusha@cachyos-pc")
    draw.text((padding_x + w1 + 8, cur_y), "~>", fill=(56, 189, 248, 255), font=font_bold)
    w2 = font_bold.getlength("~>")
    draw.text((padding_x + w1 + w2 + 18, cur_y), prompt_cmd, fill=(248, 250, 252, 255), font=font_bold)
    
    cur_y += line_height + 10
    
    # Render lines
    for item in lines_data:
        text, style = item
        if style == "header_doc":
            draw.text((padding_x, cur_y), text, fill=(56, 189, 248, 255), font=font_bold)
        elif style == "section_title":
            draw.text((padding_x, cur_y), text, fill=(251, 191, 36, 255), font=font_bold)
        elif style == "subsection":
            draw.text((padding_x + 16, cur_y), text, fill=(167, 139, 250, 255), font=font_bold)
        elif style == "highlight":
            draw.text((padding_x + 24, cur_y), text, fill=(52, 211, 153, 255), font=font_regular)
        elif style == "code":
            draw.text((padding_x + 24, cur_y), text, fill=(125, 211, 252, 255), font=font_regular)
        elif style == "dim":
            draw.text((padding_x + 24, cur_y), text, fill=(148, 163, 184, 255), font=font_regular)
        else:
            draw.text((padding_x + 24, cur_y), text, fill=(226, 232, 240, 255), font=font_regular)
        cur_y += line_height

    # Status Bar (Less / Man pager status)
    if status_bar:
        stat_h = 32
        stat_y = height - stat_h
        draw.rectangle([(0, stat_y), (width, height)], fill=(255, 255, 255, 235))
        draw.text((18, stat_y + 16), status_bar, fill=(15, 23, 42, 255), font=font_status, anchor="lm")
        
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG", quality=95)
    print(f"Generated: {output_path}")

# 1. Generate man man screenshot
man_man_lines = [
    ("MAN(1)                            Manual pager utils                           MAN(1)", "header_doc"),
    ("", "normal"),
    ("НАЗВА", "section_title"),
    ("     man - інтерфейс до довідкових посібників системи", "normal"),
    ("", "normal"),
    ("КОРОТКИЙ ОПИС (SYNOPSIS)", "section_title"),
    ("     man [man options] [[section] page ...] ...", "code"),
    ("     man -k [apropos options] regexp ...", "code"),
    ("     man -K [man options] [section] term ...", "code"),
    ("     man -f [whatis options] page ...", "code"),
    ("     man -l [man options] file ...", "code"),
    ("     man -w|-W [man options] page ...", "code"),
    ("", "normal"),
    ("ОПИС (DESCRIPTION)", "section_title"),
    ("     man — це системний пейджер довідки. Кожен page аргумент — це назва програми,", "normal"),
    ("     утиліти або системної функції. Потім знаходиться та відображається manual page.", "normal"),
    ("     Якщо вказано section, пошук обмежується лише цим розділом посібника.", "normal"),
    ("", "normal"),
    ("     Таблиця розділів системного посібника (Manual Sections):", "subsection"),
    ("     1   Виконувані програми або команди оболонки (User Commands)", "highlight"),
    ("     2   Системні виклики ядра Linux (System Calls)", "highlight"),
    ("     3   Бібліотечні виклики C / libc / POSIX (Library Calls)", "highlight"),
    ("     4   Спеціальні файли пристроїв (зазвичай у /dev)", "highlight"),
    ("     5   Формати конфігураційних файлів (/etc/passwd, fstab)", "highlight"),
    ("     6   Ігри та візуальні програми (Games)", "highlight"),
    ("     7   Різне: макроси, конвенції, стандарти (man-pages, groff)", "highlight"),
    ("     8   Команди системного адміністрування (Root / Daemons)", "highlight"),
    ("     9   Внутрішні процедури ядра [Нестандартні]", "highlight"),
]

# 2. Generate man intro screenshot
man_intro_lines = [
    ("ВСТУП(1)                         General Commands Manual                         ВСТУП(1)", "header_doc"),
    ("", "normal"),
    ("НАЗВА", "section_title"),
    ("     intro —— вступ до команд користувача (POSIX / Linux CLI)", "normal"),
    ("", "normal"),
    ("ОПИС (DESCRIPTION)", "section_title"),
    ("     У розділі 1 підручника наведено описи команд та інструментів користувача:", "normal"),
    ("     засобів для роботи з файлами, командних оболонок, компіляторів, мережевих", "normal"),
    ("     утиліт, редакторів коду, фільтрів потоків I/O та утиліт системи.", "normal"),
    ("", "normal"),
    ("ПРИМІТКИ ТА БАЗОВІ КОНЦЕПЦІЇ", "section_title"),
    ("   1. Структура команди та аргументи:", "subsection"),
    ("      $ команда [-короткі_опції] [--довгі-опції] [аргументи...]", "code"),
    ("   2. Потоки вводу/виводу та перенаправлення (I/O Redirection):", "subsection"),
    ("      stdin (0, <),  stdout (1, >, >>),  stderr (2, 2>, 2>&1)", "code"),
    ("   3. Конвеєри обробки потоків даних (Pipes |):", "subsection"),
    ("      $ cat log.txt | grep 'ERROR' | sort | uniq -c", "code"),
    ("   4. Командні оболонки (Shells):", "subsection"),
    ("      sh, bash(1), zsh(1), fish(1) — запуск процесів та інтерпретація команд.", "dim"),
]

render_terminal_screenshot(
    "/home/dusha/Шаблони/APP/man.ua/assets/man_man.png",
    "man man (uk) — Konsole",
    "man man",
    man_man_lines,
    "Manual page man(1) line 1/482 (press h for help or q to quit)"
)

render_terminal_screenshot(
    "/home/dusha/Шаблони/APP/man.ua/assets/man_intro.png",
    "man 1 intro (uk) — Konsole",
    "man intro",
    man_intro_lines,
    "Manual page intro(1) line 1/214 (press h for help or q to quit)"
)
