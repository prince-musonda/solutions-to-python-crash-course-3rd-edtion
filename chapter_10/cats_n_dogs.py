from pathlib import Path

file_names = ['dogs.txt','cats.txt']

for file in file_names:
    path = Path(file)
    try:
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'sorry, but i could not {path}')
    else:
        print(f'\nHere are the names contained in {path}:')
        print(content)

