# https://ffmpeg.org/documentation.html
# https://ffmpeg.org/download.html

"""
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libs264 -crf 23 -present ultrafast -c:a aac -b:a 320k
-c:s srt -map v:0 -map a -map 1:0 -ss 00:00:00 -to 00:00:10 "SAIDA"
"""

import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'

