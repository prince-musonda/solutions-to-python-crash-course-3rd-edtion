from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()
content = content.replace('python','C')
print(content)