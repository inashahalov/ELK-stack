import os
import re

def parse_elk_curs(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Используем регулярные выражения для поиска модулей, лабораторных, доп. материалов
    # Разбиваем по "Модуль N.", "Лабораторные работы", "Дополнительные материалы"
    # Используем ?: для несохраняющих групп
    pattern = r'(Модуль \d+\. .+?)(?=(?:Модуль \d+\. |Лабораторные работы|Дополнительные материалы|Автор курса:|$))'
    module_matches = re.findall(pattern, content, re.DOTALL)

    modules = []
    for match in module_matches:
        title_line = match.split('\n')[0]  # первая строка — заголовок
        content_part = match
        modules.append({"title": title_line, "content": [f"# {title_line}", content_part]})

    # Лабораторные работы
    lab_match = re.search(
        r'(Лабораторные работы .+?)(?=Дополнительные материалы|Автор курса:|$)',
        content,
        re.DOTALL
    )
    lab_lines = [f"# Лабораторные работы", lab_match.group(1).strip()] if lab_match else []

    # Дополнительные материалы
    extra_match = re.search(
        r'(Дополнительные материалы .+?)(?=Автор курса:|$)',
        content,
        re.DOTALL
    )
    extra_lines = [f"# Дополнительные материалы", extra_match.group(1).strip()] if extra_match else []

    return modules, lab_lines, extra_lines

def generate_chapters(modules, lab_lines, extra_lines):
    os.makedirs("docs", exist_ok=True)
    os.makedirs("docs/modules", exist_ok=True)
    os.makedirs("docs/practice", exist_ok=True)
    os.makedirs("docs/extra", exist_ok=True)

    nav = []
    for i, module in enumerate(modules, start=1):
        filename = f"module_{i:02d}.md"
        filepath = f"docs/modules/{filename}"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(module["content"]))
        nav.append({f"{module['title']}": f"modules/{filename}"})

    # Лабораторные работы
    if lab_lines:
        lab_file = "docs/practice/labs.md"
        with open(lab_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lab_lines))
        nav.append({"Лабораторные работы": "practice/labs.md"})

    # Дополнительные материалы
    if extra_lines:
        extra_file = "docs/extra/extra.md"
        with open(extra_file, "w", encoding="utf-8") as f:
            f.write("\n".join(extra_lines))
        nav.append({"Дополнительные материалы": "extra/extra.md"})

    # Главная страница
    with open("docs/index.md", "w", encoding="utf-8") as f:
        f.write("# 📘 Курс по ELK-стеку и системам наблюдаемости\n\n")
        f.write("Цель курса: подготовить инженеров к проектированию, внедрению и сопровождению современных систем наблюдаемости.\n\n")
        f.write("## Модули курса\n")
        for m in modules:
            f.write(f"- {m['title']}\n")
        f.write("\n## Практика\n")
        f.write("- Лабораторные работы\n")
        f.write("\n## Дополнительно\n")
        f.write("- Дополнительные материалы\n")

    # mkdocs.yml
    with open("mkdocs.yml", "w", encoding="utf-8") as f:
        f.write("site_name: 'ELK-стек: Образовательный курс'\n")
        f.write("theme:\n")
        f.write("  name: material\n")
        f.write("  features:\n")
        f.write("    - navigation.tabs\n")
        f.write("    - navigation.sections\n")
        f.write("    - navigation.expand\n")
        f.write("    - toc.integrate\n")
        f.write("  palette:\n")
        f.write("    scheme: slate\n")
        f.write("    toggle:\n")
        f.write("      icon: material/theme-light-dark\n")
        f.write("      name: Switch to light mode\n")
        f.write("nav:\n")
        f.write("  - 'Главная': 'index.md'\n")
        if modules:
            f.write("  - 'Модули курса':\n")
            for item in nav:
                for k, v in item.items():
                    if "Лабораторные" not in k and "Дополнительные" not in k:
                        f.write(f"    - '{k}': '{v}'\n")
        if lab_lines:
            f.write("  - 'Практика':\n")
            for item in nav:
                for k, v in item.items():
                    if "Лабораторные" in k:
                        f.write(f"    - '{k}': '{v}'\n")
        if extra_lines:
            f.write("  - 'Дополнительно':\n")
            for item in nav:
                for k, v in item.items():
                    if "Дополнительные" in k:
                        f.write(f"    - '{k}': '{v}'\n")

if __name__ == "__main__":
    modules, lab_lines, extra_lines = parse_elk_curs("ELK_curs.md")
    print("DEBUG: Modules found:", len(modules))
    print("DEBUG: Lab lines:", bool(lab_lines))
    print("DEBUG: Extra lines:", bool(extra_lines))
    generate_chapters(modules, lab_lines, extra_lines)
    print("✅ Курс успешно сгенерирован: docs/, mkdocs.yml")