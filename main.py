from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=2Q0bLo5nSsU")

audio = yt.streams.filter(only_audio=True).desc()

audio[0].download(filename=f"{yt.title}.mp3", output_path="music/")