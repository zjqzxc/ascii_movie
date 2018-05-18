from PIL import Image
import numpy as np

def image_to_ascii(img_path,img_size=(1024,768),char_size=(6,12),end_line='\r\n',ascii_chars=list(" .,:;i1tfLCG08@")):
    
    # ascii_chars = list(''' .'`^",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$''')
    # ascii_chars = list(".,:;i1tfLCG08@")
    # ascii_chars = list("@80GcLft1i;:,.")


    ascii_chars_mapping = (len(ascii_chars)-1)/255

    char_size_w,char_size_h=char_size
    max_w,max_h = img_size

    img=Image.open(img_path)

    img_w,img_h = img.size

    scale = img_w/max_w if(img_w/max_w > img_h/max_h) else img_h/max_h
    img_resize = img.resize((int(img_w / scale),int(img_h / scale))).convert('L')
    # img_resize.show()
    img_ascii = img.resize((int(img_w / scale/char_size_w),int(img_h / scale /char_size_h))).convert('L')

    img_arr = np.array(img_ascii)
    # print(img_arr)
    rst_text = ''
    for line in img_arr:
        for i in line:
            # print(,end='')
            # print(int(i * ascii_chars_mapping)-1)
            # exit();
            rst_text += ascii_chars[int(i * ascii_chars_mapping)]
        rst_text += end_line

    return rst_text
