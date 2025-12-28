import yaml
import io

with io.open('mkdocs.yml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

def get_pages(nav):
    pages = []
    if isinstance(nav, list):
        for item in nav:
            pages.extend(get_pages(item))
    elif isinstance(nav, dict):
        for key, value in nav.items():
            pages.extend(get_pages(value))
    elif isinstance(nav, str):
        if nav.endswith('.md'):
            pages.append(nav)
    return pages

all_pages = get_pages(config['nav'])
total = len(all_pages)
start = int(total * 0.11)
end = int(total * 0.15)

with io.open('pages_to_fill.txt', 'w', encoding='utf-8') as f:
    for i in range(start, end + 1):
        f.write(f"docs/{all_pages[i]}\n")
