from tkinter import *
from tkinter import filedialog
from threading import Thread
from classes import DownloadPlaylist, DownloadMusic


def select_download_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


# Playlist
def playlist_window(path):
    def start_playlist_download_thread():
        Thread(target=download_playlist).start()

    def download_playlist():
        url = playlist_url_field.get(1.0, END)
        playlist = DownloadPlaylist(url, path)
        playlist.download()

    pl_window = Toplevel(ui)
    pl_window.title("Download Playlists")
    pl_window.geometry("500x200")

    playlist_url_label = Label(pl_window, text="Paste playlist url")
    playlist_url_field = Text(pl_window, height=1, width=50)

    download_playlist_btn = Button(
        pl_window, text="Download", command=start_playlist_download_thread)

    pl_tip_label = Label(pl_window, text="Note: a playlist ends with...")

    pl_tip_label.pack()
    playlist_url_label.pack()
    playlist_url_field.pack()
    download_playlist_btn.pack()


# Music
def music_window(path):
    urls = []

    def remove_urls(urls):
        urls *= 0

    def remove_url_label_contents():
        url_field.delete(1.0, END)

    def add_url_to_file():
        urls.append(url_field.get(1.0, END))
        remove_url_label_contents()

    def start_music_download_thread():
        Thread(target=download_urls_thread).start()

    def download_urls_thread():
        music_dl = DownloadMusic(urls, path)
        music_dl.start_download_threads()

    ms_window = Toplevel(ui)
    url_label = Label(ms_window, text="Paste url")
    url_field = Text(ms_window, height=1, width=50)

    add_url = Button(ms_window, text="Add", command=add_url_to_file)

    remove_urls_btn = Button(ms_window, text="Remove all urls",
                             command=lambda: remove_urls(urls))

    download_urls = Button(ms_window, text="Download",
                           command=start_music_download_thread)

    url_label.pack()
    url_field.pack()
    add_url.pack()
    remove_urls_btn.pack()
    download_urls.pack()


ui = Tk()
ui.geometry("500x200")
ui.title('Youtube Music Downloader')

path_label = Label(
    ui, text="Select path to where files will be downloaded")
path_button = Button(ui, text="Select",
                     command=select_download_path)

music_window_btn = Button(ui, text="Download music",
                          command=lambda: music_window(path_label.cget("text")))

playlist_window_btn = Button(
    ui, text="Download Playlist", command=lambda: playlist_window(path_label.cget("text")))

path_label.pack()
path_button.pack()
music_window_btn.pack()
playlist_window_btn.pack()

ui.mainloop()
