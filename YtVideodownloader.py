# ------- Youtube Video Downloader ---- 
from pytube import YouTube
link="https://youtu.be/RgKAFK5djSk"
yt=YouTube(link)

# print(yt.thumbnail_url)
# print(yt.title)
videos=yt.streams.all()
vid=list(enumerate(videos))
for i in vid:
    print(i)
print()
strm=int(input("enter the index number you need to download : "))
print("downloading ... ")
videos[strm].download()
print("successfully Downloaded 😍")

# ------ Youtube playlist Downloader -----
# from pytube import Playlist
# link="https://www.youtube.com/watch?v=RrWyvX4lomA&list=PL3x3K5N8tSUQYc4JcWOZqbM6AomLBmLsj"

# pl=Playlist(link)
# print(f"downloading : {pl.title}")
# for video in pl.videos:
#     video.streams.first().download()
# print("downloaded successfully ")


