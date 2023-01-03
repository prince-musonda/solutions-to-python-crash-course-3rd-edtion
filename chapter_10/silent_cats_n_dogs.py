from pathlib import Path

file_names = ['cats.txt','dogs.txt']

for file in file_names:
    path = Path(file)
    try:
        content = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f'Here are the names contained in {path}:')
        print(content)