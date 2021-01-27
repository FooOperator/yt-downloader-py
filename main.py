from pytube import YouTube as yt
import validators
from pathlib import Path as p
from os import system

clear = lambda: system('cls')

class Video():
    batch = []
    
    def __init__(self, url):
        self.url = url
        self.video_title = yt(url).title
        self.video_author = yt(url).author
        self.batch.append({"Title": self.video_title, "Author": self.video_author, "URL": self.url})

    def info(self):    
        print('Title: {}\nAuthor: {}\nURL: {}'.format(self.video_title, self.video_author, self.url))
        current = yt(self.url)
        
    def download(self):
        for i in range(len(self.batch)):
            try:
                current = yt(self.batch[i]['URL'])
                print('Currently downloading: ' + self.batch[i]['Title'])
                stream = current.streams.get_by_itag(22)
                stream.download('(py)outube downloader/downloaded', filename = self.batch[i]['Title'])
                print('Dowload finished\n') 
            except:
                print('Download failed!')

clear()

while True:
    url = input('(! to download, @ to cancel and quit)\n> ')
    if validators.url(url):
        clear()
        vid = Video(url) 
        vid.info()
    elif url == '!':
        clear()
        vid.download()
        print('Operation complete, bye!')
        break
    elif url == '@':
        print('Operation cancelled, bye!')
        break
    else:
        clear()
        print('{} is invalid\n'.format(url))
