import pydub
sound = pydub.AudioSegment.from_mp3(r"C:\Users\a7825\Desktop\新建文件夹 (2)\DFO Music - Golem Tower Boss-zPOEbn3fsHw.mp4")
sound.export("test.mp3", format="mp3")
