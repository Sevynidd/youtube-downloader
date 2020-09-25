from moviepy.video.io.VideoFileClip import VideoFileClip
from pytube import YouTube

Url = input("Youtube URL: ")
pfad = input("Pfad zum Speichern: ")
mp3_or_mp4 = input("mp3 oder mp4?: ")

yt = YouTube(Url)
print("\nTitel: ", yt.title)

print("Downloading to path: ", pfad)
yt.streams.first().download(output_path=pfad, filename=yt.title)

if mp3_or_mp4 == "mp3":
    mp4_file = pfad + "\\" + yt.title + ".mp4"
    mp3_file = pfad + "\\" + yt.title + ".mp3"

    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)

    audioclip.close()
    videoclip.close()

if mp3_or_mp4 == "mp4":
    print("done")
