import os
import re

def parse_elk_curs(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Ищем все "Модуль N." и "Лабораторные работы", "Дополнительные материалы"
    modules = []
    lab_lines = []
    extra_lines = []

    # Находим модули
    module_parts = re.split(r'(Модуль \d+\. .+)', content)
    module_parts = [part.strip() for part in module_parts if part.strip()]

    i = 0
    while i < len(module_parts):
        if module_parts[i].startswith("Модуль "):
            title = module_parts[i]
            content_part = module_parts[i + 1] if i + 1 < len(module_parts) else ""
            modules.append({"title": title, "content": [f"# {title}", content_part]})
            i += 2
        else:
            i += 1

    # Находим лабораторные
    lab_match = re.search(r'(Лабораторные работы .+?)(?=Дополнительные материалы|Автор курса:|$)', content, re.DOTALL)
    if lab_match:
        lab_lines = [f"# Лабораторные работы", lab_match.group(1).strip()]

    # Находим дополнительные
    extra_match = re.search(r'(Дополнительные материалы .+?)(?=Автор курса:|$)', content, re.DOTALL)
    if extra_match:
        extra_lines = [f"# Дополнительные материалы", extra_match.group(1).strip()]

    return modules, lab_lines, extra_lines

# ... остальная часть функции generate_chapters без изменений