# ascii_movie
由视频生成字符动画

该版本目前完成度不高，暂时不能保证可以正常运行。  
如果报错，请根据错误自行修改。

## 安装
### 1、安装Python3
（略）
### 2、安装FFmpeg（并加入环境变量）
（略）
### 3、安装依赖
需要用到的python3库有flask,ffmpy3,numpy,PIL  
根据需要自行安装（如果有漏的，根据报错自行添加）


## 使用
1. ```python3 web.py```  
2. 将视频文件放入 ./statics/video文件夹  
3. 浏览器访问 http://127.0.0.1:5000/?file=abc.flv
