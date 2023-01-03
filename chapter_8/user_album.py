def make_album(artist,album_name):
    '''return a dictionary contain information about an album'''
    album = {'Artist name': artist, 'Album title': album_name}
    return album

while True:
    print('enter the name of the artist and their album')
    print('whenever you want to quit enter "q":')
    artist = input('Artist name: ')
    if artist.lower() == 'q':
        break

    album_name = input('Album title: ')
    if album_name.lower() == 'q':
        break

    album_info = make_album(artist,album_name)
    print(album_info)