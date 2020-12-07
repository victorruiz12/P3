
import os
import subprocess
def py2():

    print("How many files do you want?:" )
    num_files = input()
    files = []
    channels = []
    n = int(num_files)
    print("Name the files (with extension) and the number of channels:")
    for k in range(n):
        print("File" + str(k+1) + ":")
        file_name = input()
        files.append(file_name)
        print("Channels:")
        channel_num = input()
        channels.append(channel_num)

    for k in range(n):
        name = "ffmpeg -i {} ".format(files[k])

    copy_codecs = name + "-c copy"

    for k in range(n):
        for i in range(int(channels[k])):
            name = name + "-map {}:{} ".format(k,i)

    name = str(name + "_cont.mp4")
    print(name)

    subprocess.call(name, shell=True)

if __name__ == "Lab3":
    py2()