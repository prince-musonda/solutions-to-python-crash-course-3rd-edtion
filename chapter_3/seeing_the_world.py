places = ['new york city','paris','motriel','japan','london']

print('places i would like to go to, original list:')
print(places)
print('same list sorted but not temporary:')
print(sorted(places))
print('it is not sorted permanently, look:')
print(places)
print(' i am reversing the original order:')
places.reverse()
print(places)
print('i am reversing it once more and bring in it back:')
places.reverse()
print(places)
print('i am now going to sort it alphabetically, permanently!!!')
places.sort()
print(places)
print('i am now reversing it alphabetically and permanently: ')
places.sort(reverse=True)
print(places)