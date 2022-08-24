from pytube import Playlist
from pytube import YouTube
from threading import Thread


class DownloadPlaylist():

    def __init__(self, url, path):
        self.playlist = Playlist(url)
        self.title = self.playlist.title.replace(" ", "_").replace(":", "")
        self.path = path

    def delete_url(self):
        self.playlist = None

    def download(self):
        for video in self.playlist.videos:
            print("Downloading", video.title)
            dl = video.streams.filter(progressive=True).desc()
            dl[0].download(output_path=self.path +
                           f"/playlist_yt_dl/{self.title}/")
            print("Finished")


class DownloadMusic():

    def __init__(self, urls, path):
        self.urls = urls
        self.path = path + "/music_yt_dl/"

    def delete_urls(self):
        self.urls *= 0

    def download_urls(self, url):
        print("Downloading:", url)

        yt = YouTube(url)
        title = yt.title.replace(" ", "_").replace(":", "")
        audio = yt.streams.filter(only_audio=True).desc()
        audio[0].download(
            filename=f"{title}.mp3", output_path=self.path)
        print("Finished:")

    def start_download_threads(self):
        threads = [Thread(target=self.download_urls, args=(url, ))
                   for url in self.urls]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.delete_urls()
