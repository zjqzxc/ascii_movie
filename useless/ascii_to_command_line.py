from image_to_ascii import image_to_ascii
import time

ts_start=88000
ts_end=98000

duration=10000
fps = 5
offset = int(1/fps * 1000)
sleep_second = int(1/fps)

while ts_start <= ts_end:
    ms = str(ts_start%1000)
    real_s = int(ts_start/1000)
    h=str(int(real_s/3600))
    m=str(int((real_s%3600)/60))
    s=str(int((real_s%60)))
    
    time_str = h+'_'+m+'_'+s+'.'+ms
    print(image_to_ascii('./tmp/'+time_str + '.jpg'))

    ts_start += offset
    time.sleep(sleep_second)
