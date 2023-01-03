def make_album(artist,album_name,songs_num = None):
    '''return a dictionary contain information about an album'''
    album = {'Artist name': artist, 'Album title': album_name}
    if songs_num:
        album['number of songs'] = songs_num
    return album


album  = make_album('john cena', 'you can\'t see me',10)
print(album)

another_album = make_album('abel chung','worship of the love')
print(another_album)

another_album_2 = make_album('abel chungu','worship of the love revolution')
print(another_album_2)

