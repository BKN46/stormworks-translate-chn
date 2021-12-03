import json

from PIL import Image, ImageSequence

im = Image.open("test.gif")
resize_param = 0.64
width = round(im.size[0] * resize_param)
height = round(im.size[1] * resize_param)

print(width, height)

code_seq = "".join([chr(i) for i in range(48, 123)])
comp_ratio = 64


def rgb_comp(rgb):
    trans = lambda x: int(x / comp_ratio) * comp_ratio
    return (trans(rgb[0]), trans(rgb[1]), trans(rgb[2]))


def rgb_to_code(rgb):
    ratio_rev = int(256 / comp_ratio)
    normal = lambda x: int(x / comp_ratio)
    seq = normal(rgb[0]) * ratio_rev ** 2 + normal(rgb[1]) * ratio_rev + normal(rgb[2])
    # return seq
    return code_seq[seq]


def vm_encode(vm):
    return "/".join(
        ["|".join(["".join([str(i) for i in row]) for row in frame]) for frame in vm]
    )


def bm_to_vec(bm):
    bm = bm.split("\n")
    res = []
    # seq_encode = lambda x: x
    seq_encode = lambda x: code_seq[x]
    for row in bm:
        now_color = ""
        row_res = []
        for i, char in enumerate(row):
            if now_color == "":
                now_color = char
            elif char != now_color:
                row_res.append(seq_encode(i))
                row_res.append(now_color)
                now_color = char
            elif i == len(row) - 1:
                row_res.append(seq_encode(i))
                row_res.append(now_color)
        res.append(row_res)
    return res


def code_to_rgb(code):
    code = ord(code) - 48
    ratio_rev = int(256 / comp_ratio)
    return (
        comp_ratio * (int(code / ratio_rev / ratio_rev) % ratio_rev),
        comp_ratio * (int(code / ratio_rev) % ratio_rev),
        comp_ratio * (code % ratio_rev),
    )


def get_img_array(img):
    res = []
    pixels = img.load()
    for h_p in range(img.height):
        res_w = []
        for w_p in range(img.width):
            pix_r, pix_g, pix_b = img.getpixel((w_p, h_p))
            trans_rgb = rgb_comp((pix_r, pix_g, pix_b))
            pixels[w_p, h_p] = trans_rgb
            res_w.append(rgb_to_code(trans_rgb))
        res.append(res_w)
    return res


if __name__ == "__main__":
    frame_s, frame_e = None, []
    last_img_str = ""
    vm_res = []
    for index, frame in enumerate(ImageSequence.Iterator(im)):
        frame = frame.resize((width, height)).convert("RGB")
        frame_bm = get_img_array(frame)
        # frame.save(f"frames/{index}.png")

        img_str = "\n".join(["".join([str(y) for y in x]) for x in frame_bm])
        vm_res.append(bm_to_vec(img_str))
        # Drop repeated frame
        # if img_str == last_img_str:
        #     continue
        # last_img_str = img_str

        if not frame_s:
            frame_s = frame
        else:
            frame_e.append(frame)

    frame_s.save(
        "test_out.gif", save_all=True, append_images=frame_e, duration=20, loop=0
    )
    open("gif/test.vm", "w").write(vm_encode(vm_res))
