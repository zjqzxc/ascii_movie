import ffmpy3
import os
import subprocess
import re
import datetime


class FFmpegPy3():
    def __init__(self, outputh_path = ''):
        self.outputh_path = outputh_path if outputh_path else '.\\'

    def getDuration(self,filename,ts=False):
        result = subprocess.Popen(["ffprobe", filename],
        stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        # for x in result.stdout.readlines():
        #     print(x.decode())
        duration_str = [x.decode() for x in result.stdout.readlines() if "Duration" in x.decode()]
        if duration_str:
            # s = re.findall(r'Duration: .*?,',duration_str[0])
            s = re.findall(r'\d+:\d+:\d+\.\d+',duration_str[0])[0]
        
        if ts:
            dtime = datetime.datetime.strptime(s,'%H:%M:%S.%f')
            duration = dtime.hour*3600 + dtime.minute*60 + dtime.second + dtime.microsecond/1000000
            duration *= 1000
            return int(duration)
        else:
            return s

    def snap(self,input_file,time_offset,file_name=None):
        dir_path = os.path.join('.\\',self.outputh_path)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)

        if file_name == None:
            file_name = time_offset.replace(':','_')

        output_file = os.path.join(dir_path,file_name + '.jpg');
        ff = ffmpy3.FFmpeg(
            inputs={input_file:'-ss ' + time_offset},
            outputs={output_file:' -r 1 -vframes 1 -an -f mjpeg -y'}
            )
        # print(ff.cmd)
        ff.run()

    def getAudio(self,input_file,output_file_name):
        dir_path = os.path.join('.\\',self.outputh_path)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)

        output_file = os.path.join(dir_path,output_file_name + '.ogg');
        ff = ffmpy3.FFmpeg(
            inputs={input_file:None},
            outputs={output_file:' -vn -f ogg -y'}
            )
        # print(ff.cmd)
        ff.run()  

