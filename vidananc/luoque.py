import json
with open('luoque.json', 'r') as f:
    dict = json.load(f)
    print(dict['luoque'])