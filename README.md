## Plalist audio downloader

<img src="https://i.imgur.com/GdjY8tH.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="50" height="50" /> <img src="https://img.shields.io/badge/youtube--dl-playlist%20audio%20downloader-red"> <img src="https://img.shields.io/static/v1?label=platform&message=macosx|linux&color=lightgray">

- [INSTALLATION](#installation)
- [USAGE](#usage)

# INSTALLATION
Requires youtube-dl. You can download install following the instructions at the [youtube-dl github page](https://github.com/ytdl-org/youtube-dl/blob/master/README.md), or open the `install.py` file with python.
#### McOSX Installation
1. Open your terminal (you can search for "terminal" with Spotlight Search)
2. Go to the folder where you have downloaded the file and unzip it (if necessary)
3. Type `cd` into the terminal and drag the folder youtubeplaylistaudio-master into it. If you have downloaded the file into the Downloads folder, your terminal command should look something like this:

       cd /Users/[YOUR_USERNAME]/Downloads/youtubeplaylistaudio-master
4. Copy this command into your terminal:

       python install.py
#### Linux installation
1. Using your terminal,`cd` into the folder you downloaded the repository
2. Copy the following into the terminal

       python3 install.py

# USAGE
Open the playlist audio downloader by going into the folder where it is at and typing into the terminal:

       python youtubedl.py
or

       python3 youtubedl.py
Paste the link to your playlist.
Next you can give it the name of the folder where to put the songs. If the folder doesn't exists, it will create a folder with the name given. *Please note that you cannot use spaces, so instead of writing 'playlist name', write 'playlist_name' instead*.
For Linux users: if you get the error:

       /usr/bin/env: 'python': No such file or directory
Copy the following command into your terminal:

       sudo ln -s /usr/bin/python3 /usr/bin/python
