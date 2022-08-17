from tkinter import *
from tkinter import filedialog
import os
import threading 
from pytube import YouTube


def select_download_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def add_url_to_file():

    if os.path.exists("youtube_urls.txt"):

        with open("youtube_urls.txt", "a") as file:
            file.write(url_field.get(1.0, END))

    else:
        with open("youtube_urls.txt", "w") as file:
            file.write(url_field.get(1.0, END))

    url_field.delete(1.0, END)


def remove_file_contents():
    with open("youtube_urls.txt", "w") as file:
        file.truncate()


def download():
    with open("youtube_urls.txt", "r") as file:
        for url in file:
            yt = YouTube(url)
            audio = yt.streams.filter(only_audio=True).desc()
            audio[0].download(
                filename=f"{yt.title}.mp3", output_path=path_label.cget("text"))


def start_download_thread():
    threading.Thread(target=download).start()


ui = Tk()
ui.geometry("500x200")
ui.title('Youtube Music Downloader')

url_label = Label(ui, text="Paste url")
url_field = Text(ui, height=1, width=50)

add_url = Button(ui, text="Add", command=add_url_to_file)

remove_urls = Button(ui, text="Remove all urls", command=remove_file_contents)

download_urls = Button(ui, text="Download", command=start_download_thread)

path_label = Label(ui, text="Select path to where files will be downloaded")
path_button = Button(ui, text="Select", command=select_download_path)

path_label.pack()
path_button.pack()
url_label.pack()
url_field.pack()
add_url.pack()
remove_urls.pack()
download_urls.pack()

ui.mainloop()
