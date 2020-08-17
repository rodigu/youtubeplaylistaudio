import os
import pathlib

# test link playlist:
# PLlbHPr1oifB9DyiTzQMhIVGINiCMzbGaG
# https://www.youtube.com/playlist?list=PLlbHPr1oifB9DyiTzQMhIVGINiCMzbGaG
link = input("Playlist link: ")
write = "youtube-dl " + link + " -i -f 140"
filename = input("Name for the file: ")
create = "mkdir " + filename
os.system(create)
PATH = str(pathlib.Path(__file__).parent.absolute()) + '/' + filename
download = "youtube-dl -i -f 140 -o " + PATH + "/%\(title\)s.%\(ext\)s " + link
os.system(download)
