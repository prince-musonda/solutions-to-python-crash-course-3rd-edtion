from pathlib import Path
import json

number = input('tell me your favourite number, and i will never forget it: ')
path = Path('favourite_number.json')
content = json.dumps(number)
path.write_text(content)
