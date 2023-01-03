from pathlib import Path
import json

path = Path('favourite_number.json')
content = path.read_text()
favourite_number = json.loads(content)

print(f'i know your favourite number, it is {favourite_number}')
