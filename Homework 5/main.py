import MusicDB

MusicDB.help()
while(True):
    choice = input(">")
    if (choice == "help"):
        MusicDB.help()
    if (choice == "exit"):
        break

