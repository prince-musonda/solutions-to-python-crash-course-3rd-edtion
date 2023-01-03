from pathlib import Path
names = ''
while(True):
    name = input('\t\tEnter your name and press enter.\n\t\twhen you are all done\
entering your names, type "done" to exit the program.\nName: ')
    if name == 'done':
        break
    else:
        names += name +'\n'

path = Path('guest_book.txt')
path.write_text(names)