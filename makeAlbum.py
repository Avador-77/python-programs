def make_album(artist, album, n_of_tracks = ''):

    if n_of_tracks == '':
        info = {'Artist Name':artist.title(),'Album Title':album.title()}
    else:
        info = {'Artist Name':artist.title(),'Album Title':album.title(),'No Of Tracks':int(n_of_tracks)}

    return info


while True:
    
    artistName = input("(Press 'q' anytime to quit)\nEnter the name of the artist: ")
    if artistName == 'q':
        break

    albumName = input("(Press 'q' anytime to quit)\nEnter the name of the album: ")
    if albumName == 'q':
        break

    tracksCount = input("(Press 'q' anytime to quit)\nEnter the number of tracks(Press enter if you don't know): ")
    if tracksCount == 'q':
        break
    album_info = make_album(artistName, albumName, tracksCount)

    print(album_info)