from PIL import Image
import numpy as np
from FFmpegPy3 import FFmpegPy3
import datetime
import time

class AsciiMovie():
    
    def imageToAscii(self,img_path,img_size=(1024,768),char_size=(6,12),end_line='\r\n',ascii_chars=list(" .,:;i1tfLCG08@")):
        
        ascii_chars_mapping = (len(ascii_chars)-1)/255

        char_size_w,char_size_h=char_size
        max_w,max_h = img_size

        img=Image.open(img_path)

        img_w,img_h = img.size

        scale = img_w/max_w if(img_w/max_w > img_h/max_h) else img_h/max_h
        # img_resize = img.resize((int(img_w / scale),int(img_h / scale))).convert('L')
        # img_resize.show()
        img_ascii = img.resize((int(img_w / scale/char_size_w),int(img_h / scale /char_size_h))).convert('L')

        img_arr = np.array(img_ascii)
        rst_text = ''
        for line in img_arr:
            for i in line:
                rst_text += ascii_chars[int(i * ascii_chars_mapping)]
            rst_text += end_line

        return rst_text

    def videoToSnap(self,file_name):
        t=FFmpegPy3().getDuration('./statics/video/'+file_name)
        dtime = datetime.datetime.strptime(t,'%H:%M:%S.%f')
        duration = dtime.hour*3600 + dtime.minute*60 + dtime.second + dtime.microsecond/1000000
        duration *= 1000

        ts_start=0
        ts_end=duration

        fps = 5
        offset = int(1/fps * 1000)

        while ts_start <= ts_end:
            ms = str(ts_start%1000)
            real_s = int(ts_start/1000)
            h=str(int(real_s/3600))
            m=str(int((real_s%3600)/60))
            s=str(int((real_s%60)))
            
            time_str = h+':'+m+':'+s+'.'+ms
            FFmpegPy3('snap/'+file_name).snap('./statics/video/'+file_name,time_str)

            ts_start += offset
