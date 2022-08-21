from tkinter import *
from tkinter import filedialog
from threading import Thread
from pytube import YouTube


urls = []


def select_download_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def remove_url_label_contents():
    url_field.delete(1.0, END)


def add_url_to_file():

    urls.append(url_field.get(1.0, END))
    remove_url_label_contents()


def remove_file_contents(urls):
    urls *= 0
    remove_url_label_contents()


def download(url, index):
    print("started:", url)

    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).desc()
    audio[0].download(
        filename=f"{index}.mp3", output_path=path_label.cget("text") + "/yt_downloader/")
    print("finished:", index)


def download_urls_thread():
    threads = [Thread(target=download, args=(url, index))
               for index, url in enumerate(urls)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def start_download_thread():
    Thread(target=download_urls_thread).start()


ui = Tk()
ui.geometry("500x200")
ui.title('Youtube Music Downloader')

url_label = Label(ui, text="Paste url")
url_field = Text(ui, height=1, width=50)

add_url = Button(ui, text="Add", command=add_url_to_file)

remove_urls = Button(ui, text="Remove all urls",
                     command=lambda: remove_file_contents(urls),)

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
