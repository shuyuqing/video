import os
from moviepy.editor import *
video = VideoFileClip(os.path.join("path","to","movie.mp4"))
video.audio.write_audiofile(os.path.join("path","to","movie_sound.mp3"))

# 批量将mp4视频转换成mp3音频

from pathlib import Path			# 管理文件和文件夹的第三方模块
from moviepy.editor import *		# 视频处理模块

p = Path('/Users/shiying/Documents/课堂外的读本/乡风市声')
# p指向存放mp4视频的文件夹

q = p.joinpath('mp3')
q.mkdir(mode=0o777, exist_ok=True)
# 在存放mp4视频的文件夹下建立一个叫做mp3的文件夹，赋予全部权限
#（mode=0o777），即使mp3文件夹已经存在也不报错（exist_ok=True）

for i in p.glob('*'):
# 遍历p所指向的文件夹下的每个视频

    audioName = i.stem + '.mp3'
    # 音频文件名存放在变量audioName，i.stem得到文件i的扩展名
    audioFile = q.joinpath(audioName)
    # audioFile指向未来生成的音频文件

    if i.suffix in ['.mp4','mov','webm','flv','avi'] and not audioFile.exists():
    # 如果i指向的是列表内格式的视频并且它的mp3音频文件在mp3文件夹里不存在
        video = VideoFileClip(str(i))
        # 生成视频对象，参数是视频文件的路径字串+文件名
	   # 直接放路径对象i会报错，只好转成路径字串放进去
        video.audio.write_audiofile(audioFile)
        # 视频中的音频取出，保存成文件
	   # 若是在windows上，参数放文件对象audioFile会出错
	   # 需要str(audioFile) 转成字符串