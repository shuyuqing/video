from __future__ import unicode_literals
import youtube_dl

# ydl_opts = {}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=9SmLoTRnGY4'])

from pydub import AudioSegment


filepath = r"C:\Users\a7825\Desktop\新建文件夹 (2)\DFO Music - Golem Tower Boss-zPOEbn3fsHw.mp4"
song = AudioSegment.from_mp3(filepath)
song.export("now.mp3", format="mp3")