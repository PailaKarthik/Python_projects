from moviepy.editor import *
from tkinter.filedialog import *

vid=askopenfilename()
video=VideoFileClip(vid)
aud=video.audio
aud.write_audiofile("1.mp3")
print("succesfully converted 😍")