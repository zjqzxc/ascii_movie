from flask import Flask,render_template,request
from image_to_ascii import image_to_ascii
import json
import os
from FFmpegPy3 import FFmpegPy3
from AsciiMovie import AsciiMovie

app = Flask(__name__)
app._static_folder = './statics'


@app.route('/')
def index():
    
    try:
        file_name = request.args.get('file')
    except:
        file_name = 'wsyw.flv'
    if not os.path.isdir('./snap/'+file_name):
        return '截图未生成,请使用命令行运行:pyhton3 snap.py '+file_name
    try:
        start = int(request.args.get('start'))
    except:
        start = 0
    try:
        end = int(request.args.get('end'))
    except:
        end = FFmpegPy3().getDuration('./statics/video/wsyw.flv',True)


    return render_template('index.html',
    title='Ascii Movie',
    video=file_name,
    audio=file_name,
    start=start,
    end=end,
    fps='5')
    # return '<style>html{font-family: Consolas, Monaco, monospace;}</style>' + image_to_ascii('./img/wsyw.jpg',img_size=(800,600),char_size=(8.75,15.5),end_line='<br/>',ascii_chars = list("@80GcLft1i;:,."))


@app.route('/getascii')
def getascii():
    file = request.args.get('file')
    ts_start = int(request.args.get('start'))
    ts_end = int(request.args.get('end'))
    fps = int(request.args.get('fps'))

    # duration=167000
    # if ts_end > duration:
    #     return 'eof'
    
    offset = int(1/fps * 1000)
    sleep_second = int(1/fps)

    rst = dict()
    rst['info']={
        'file':file,
        'start':ts_start,
        'end':ts_end,
        'fps':fps
    }

    while ts_start <= ts_end:
        ms = str(ts_start%1000)
        real_s = int(ts_start/1000)
        h=str(int(real_s/3600))
        m=str(int((real_s%3600)/60))
        s=str(int((real_s%60)))
        
        time_str = h+'_'+m+'_'+s+'.'+ms
        rst[ts_start] = AsciiMovie().imageToAscii('./snap/'+file+'/'+time_str + '.jpg',img_size=(1024,768),char_size=(8.75,14),end_line='<br/>',ascii_chars = list(".,:;i1tfLCG08@"))

        ts_start += offset

    return json.dumps(rst)


if __name__ == '__main__':
    app.debug = True
    app.run()