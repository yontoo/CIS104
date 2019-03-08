def help():
    print("Commands in this program:")
    print("1. add - Add a new song to the database.")
    print("2. list - List the songs in the database.")
    print("3. save - Save the songs to the database.")
    print("4. clear - Clear the current songs inside of the database.")
    print("5. help - Display this menu again.")
    print("6. exit - Close program.")

def add():
    song = input("Enter song title: ")
    artist = input("Enter artist: ")
    album = input("Enter album: ")
    trk_num = int(input("Enter track #: "))
    song_year = int(input("Enter release year: "))
    genre = input("Enter genre: ")

#https://python-forum.io/Thread-Looping-to-Create-Nested-Dictionary
    add_songs = dict(dict_song = song, dict_art = artist, dict_album = album, dict_trknum = trk_num, dict_year = song_year, dict_genre = genre)
buncha_songs = {
    "Song1": 
}

