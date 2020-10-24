import youtube_dl    # 先安装第三方模块youtube-dl

audioFile = r"C:/Users/a7825/Desktop/s/"
# 音频文件存放的目标字串

# 下载视频的链接，油管有提供视频对应的音频
videoPage = 'https://www.youtube.com/playlist?list=PLUJ4RSS4ZmuKTrPmalEAFLdRQlZiZPSi5'

ydl_opts = {            # ydl_opts很重要，是个字典，所有参数在这里设置
            'outtmpl': audioFile+'%(title)s.%(ext)s',
            # 定义输出模版：指定输出的文件夹+保存的文件名
            # title：视频的标题，比如将多个pdf文件合并成一个；ext：扩展名，比如m2a
            # 所以视频或音频的文件名就是：将多个pdf文件合并成一个.m2a
            'format': 'bestaudio',
            # 不止一个音频文件时，选择音质最好(format标注为bestaudio)的音频下载
            # 但是如果视频网站没有提供对应的音频文件，则会报错
            }
ydl = youtube_dl.YoutubeDL(ydl_opts)        # 生成下载对象

ydl.download([videoPage])
    # 下载视频，参数是列表，列表的每个元素是视频的链接