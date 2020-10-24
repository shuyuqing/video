import youtube_dl
import ffmpeg

audioFile = 'C:/Users/a7825/Desktop/s/'
# 音频文件存放的目标字串

# 下载视频的链接
videoPage = 'https://www.youtube.com/watch?v=qJBeQf2BQK8'
# videoPage = 'https://www.youtube.com/watch?v=FLhzB_DJQb4'

ydl_opts = {            # ydl_opts很重要，是个字典，所有参数在这里设置
            'outtmpl': audioFile+'%(title)s.%(ext)s',
            # 定义输出模版

            'postprocessors': [
                {'key': 'FFmpegExtractAudio',
                 # 指定用FFmpeg从视频中提取音频
                 'preferredcodec': 'mp3',
                 # 指定音频格式
                 },
            ],

            'keepvideo': True,
            # 默认视频转换成音频后删掉视频文件
            # 设置为True后不删除视频，测试时反复运行，视频不必每次都下载
            }
ydl = youtube_dl.YoutubeDL(ydl_opts)        # 生产下载对象

with ydl:
    ydl.download([videoPage])               # 下载视频