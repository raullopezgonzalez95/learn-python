from pytube import YouTube as yt

link = input('Youtube Video URL: ')
video_download = yt(link)
video_download.streams.first().download()
print('Video Downloaded')
