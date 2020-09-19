import os
import pathlib

link = input("Playlist link: ")
write = "youtube-dl " + link + " -i -f 140"
filename = input("Name for the file: ")
create = "mkdir " + filename
os.system(create)
PATH = str(pathlib.Path(__file__).parent.absolute()) + '/' + filename
download = "youtube-dl -i -f 140 -o " + PATH + "/%\(title\)s.%\(ext\)s " + link
os.system(download)
