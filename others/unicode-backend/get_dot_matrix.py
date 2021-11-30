import pickle
import json

bm_data = pickle.loads(open('DinkieBitmap-7pxDemo.ttf.bm', 'rb').read())

def toUnicode(oneStr):
    t=oneStr
    # if  t[:3] == 'uni':t=t.replace('uni','\\u') 
    # if  t[:2] == 'uF':t=t.replace('uF','\\u') 
    return json.loads(f'"\\u{t}"') 

def bm_to_vec(bm):
    bm = bm.split('\n')
    res = []
    for row in bm:
        is_line = False
        row_res = []
        for i, char in enumerate(row):
            if char == '0' and not is_line:
                is_line = True
                row_res.append(i)
            elif char == '1' and is_line:
                row_res.append(i-1)
                is_line = False
            elif char == '0' and i == len(row)-1:
                row_res.append(i)
                if not is_line:
                    row_res.append(i)
        res.append(row_res)
    return res

def get_render(vm):
    bm = ['0'*len(vm[0])]*7
    for ri, row in enumerate(vm):
        for i in range(0, len(row)-1, 2):
            bm[ri] = bm[ri][:row[i]] + '1'*(row[i+1]-row[i]+1) + bm[ri][row[i+1]+1:]
    return '\n'.join(bm).replace('0', '□').replace('1', '■')

def multiple_bit_to_vec(text):
    # print(text)
    res = ['' for _ in range(7)]
    for chr in text:
        if chr in bm_data:
            bm = bm_data[chr].split('\n')
        else:
            bm = bm_data[' '].split('\n')
        for i in range(7):
            res[i] = res[i] + '1' + bm[i]
    # print('\n'.join(res))
    return bm_to_vec('\n'.join(res))

def unicode_bit_to_vec(text):
    text = ''.join([toUnicode(x) for x in text])
    print(text)
    res = multiple_bit_to_vec(text)
    print(get_render(res))
    return res

if __name__ == "__main__":
    # print(toUnicode('\\u0042'))
    pass
    # print(multiple_bit_to_vec("\u4f60\u597d"))
    # print(unicode_bit_to_vec("\u4f60\u597d"))
