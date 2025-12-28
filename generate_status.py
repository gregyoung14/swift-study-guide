import yaml
import io
import os
import json
import re

def get_pages(nav):
    pages = []
    if isinstance(nav, list):
        for item in nav:
            pages.extend(get_pages(item))
    elif isinstance(nav, dict):
        for key, value in nav.items():
            if isinstance(value, str):
                if value.endswith('.md'):
                    pages.append(value)
            else:
                pages.extend(get_pages(value))
    elif isinstance(nav, str):
        if nav.endswith('.md'):
            pages.append(nav)
    return pages

def analyze_page(filepath):
    if not os.path.exists(filepath):
        return False
    
    try:
        with io.open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Criteria for "completed"
        # 1. Word count > 100
        words = re.findall(r'\w+', content)
        word_count = len(words)
        
        # 2. Presence of code blocks
        has_code = '```' in content
        
        # 3. Presence of multiple headers (indicating structure)
        headers = re.findall(r'^#{2,4} ', content, re.MULTILINE)
        has_structure = len(headers) >= 2
        
        # A page is completed if it has substantial content (+100 words) 
        # AND (has code OR has structure)
        # Or if it's very long (+300 words)
        is_completed = (word_count > 100 and (has_code or has_structure)) or (word_count > 300)
        
        return is_completed
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False

def main():
    try:
        with io.open('mkdocs.yml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        all_pages = get_pages(config['nav'])
        
        status_db = []
        for i, page_path in enumerate(all_pages):
            full_path = os.path.join('docs', page_path)
            is_completed = analyze_page(full_path)
            
            status_db.append({
                "id": i,
                "path": page_path,
                "completed": is_completed,
                "status": "completed" if is_completed else "pending"
            })
            
        with io.open('pages_status.json', 'w', encoding='utf-8') as f:
            json.dump(status_db, f, indent=4)
            
        print(f"Successfully generated status for {len(status_db)} pages.")
        
    except Exception as e:
        print(f"Failed to generate status: {e}")

if __name__ == "__main__":
    main()
