import json
with open('luoque.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
    print(d['luoque'])
