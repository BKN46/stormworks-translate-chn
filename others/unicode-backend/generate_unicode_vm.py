import pickle
import json

from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from tqdm import tqdm
# import fontTools

size = 7
# use a truetype font
font_path = "DinkieBitmap-7pxDemo.ttf"
font = ImageFont.truetype(font_path, size+1)

def toUnicode(oneStr):
    t=oneStr
    if  t[:3] == 'uni':t=t.replace('uni','\\u') 
    if  t[:2] == 'uF':t=t.replace('uF','\\u') 
    return json.loads(f'"{t}"') 

def get_all_char():
    font = TTFont(font_path)
    res = []
    for c in font.getGlyphOrder():
        if c == '.notdef':
            continue
        res.append(c)
    return res

def get_img_array(img, w, h):
    res = []
    for h_p in range(h):
        res_w = []
        for w_p in range(w):
            rgb = img.getpixel((w_p, h_p))
            if rgb == 0:
                res_w.append(0)
            else:
                res_w.append(1)
        res.append(res_w)
    return res

def gen_text_img(text):
    img_width = size*len(text)
    img_height = size
    image = Image.new("1", (img_width, img_height), (1))
    draw = ImageDraw.Draw(image)
    draw.text((0, -2), text, font=font)
    res = get_img_array(image, img_width, img_height)
    text_res = '\n'.join([''.join([str(y) for y in x]) for x in res])
    # print(text_res)
    # image.save("test.png")
    return text_res

if __name__ == "__main__":
    # gen_text_img("丁")
    res = {}
    extra_char = [' ']
    for chr in tqdm(extra_char + get_all_char()):
        chr = toUnicode(chr)
        if len(chr) > 1:
            continue
        chr_bitmap = gen_text_img(chr)
        res[chr] = chr_bitmap

    open(font_path+'.bm', 'wb').write(pickle.dumps(res))
