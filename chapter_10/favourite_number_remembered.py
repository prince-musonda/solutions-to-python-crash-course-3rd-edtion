from pathlib import Path
import json

path = Path('favourite_number.json')

if path.exists():
     content = path.read_text()
     favourite_number = json.loads(content)
     print(f'i know your favourite number, it is {favourite_number}')
else:
    favourite_number = input('tell me your favourite number and i will never never forget it\nfavourite number: ')
    content = json.dumps(favourite_number)
    path.write_text(content)