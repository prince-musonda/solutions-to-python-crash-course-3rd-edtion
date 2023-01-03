from pathlib import Path

name = input('what is your name? ')
path = Path('guest_name.txt')
path.write_text(name.strip().title())