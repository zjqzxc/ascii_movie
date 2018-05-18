import os,sys
from AsciiMovie import AsciiMovie
from FFmpegPy3 import FFmpegPy3

if (len(sys.argv) == 2):
    file_path = os.path.join('./statics/video',sys.argv[1])
    if(os.path.exists(file_path)):
        AsciiMovie().videoToSnap(sys.argv[1])
        FFmpegPy3().getAudio('./statics/video/'+sys.argv[1],'./statics/audio/'+sys.argv[1])
    else:
        print('file does not exist,please copy your video in ./statics/video folder')
    
else:
    print('Usage:\r\n python3 snap.py filename')