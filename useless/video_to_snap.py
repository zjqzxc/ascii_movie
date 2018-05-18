from FFmpegPy3 import FFmpegPy3
import datetime
import time

t=FFmpegPy3().getDuration('wsyw.flv')
dtime = datetime.datetime.strptime(t,'%H:%M:%S.%f')
duration = dtime.hour*3600 + dtime.minute*60 + dtime.second + dtime.microsecond/1000000
duration *= 1000

ts_start=0
ts_end=219000

fps = 5
offset = int(1/fps * 1000)

while ts_start <= ts_end:
    ms = str(ts_start%1000)
    real_s = int(ts_start/1000)
    h=str(int(real_s/3600))
    m=str(int((real_s%3600)/60))
    s=str(int((real_s%60)))
    
    time_str = h+':'+m+':'+s+'.'+ms
    FFmpegPy3('tmp').snap('badapple.flv',time_str)

    ts_start += offset