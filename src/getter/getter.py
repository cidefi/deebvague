from __future__ import unicode_literals
import youtube_dl

class Logger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def progress_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': Logger(),
    'progress_hooks': [progress_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=UF0l4qGMi1Y'])