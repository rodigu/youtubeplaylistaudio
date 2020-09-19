import os
import sys

print("OS Detected: ", sys.platform, "\n")
if (sys.platform == "linux"):
    os.system("sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl")
    os.system("sudo chmod a+rx /usr/local/bin/youtube-dl")
elif (sys.platform == 'darwin'):
    os.system("sudo xcode-select --install")
    os.system("/bin/bash -c $(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)")
    os.system("brew install wget")
    os.system("sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl")
    os.system("sudo chmod a+rx /usr/local/bin/youtube-dl")
else:
    print("Only Linux and MacOSX are supported currently\n")
