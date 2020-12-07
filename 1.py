#1) You’re going to create a new BBB container:

import subprocess
import os

def py1():

    #cut video 1 min
    subprocess.call('ffmpeg -ss 00:00:00 -i bbb_original_video.mp4 -t 00:00:59 -c copy bbb_1min_video.mp4', shell=True)
    #extract audio
    subprocess.run('ffmpeg -i bbb_1min_video.mp4 -acodec copy bbb_1min_audio.ac3', shell=True)

    #To output just 1 audio channel, i.e. mono. By default this operation
    #will preserve the file format but bitrate = 64kbps (lower bitrate)

    #si quisieramos aumentarlo, por ejemplo, a 192 kbps:
    #ffmpeg -i file.ext -ac 1 -ab 192k file_mono.ext

    #extract mono audio in lower bitrate
    subprocess.run('ffmpeg -i bbb_1min_audio.ac3 -ac 1 bbb_1min_audio_mono.ac3', shell=True)

    #convert subtitles to .ass format
    os.system("ffmpeg -i subtitles.srt subtitles.ass")

    #add subtitles
    os.system('ffmpeg -i bbb_1min_video.mp4 -vf "ass=subtitles.ass" bbb_1min_video_subs.mp4')

    #all in one container
    os.system('ffmpeg -i bbb_1min_video.mp4 -i bbb_1min_audio.ac3 -i bbb_1min_audio_mono.ac3 \
            -map 0:0 -map 0:1 -map 1:0 -map 2:0 -vf \
            "ass=subtitles.ass" bbb1_1min_container.mp4')

if __name__ == "Lab3":
    py1()