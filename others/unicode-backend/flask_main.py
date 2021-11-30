from flask import Flask, request

from get_dot_matrix import unicode_bit_to_vec

app = Flask(__name__)

@app.route("/swchr")
def get_chn():
    origin_value = request.args.get("text") or ''
    value = origin_value.split('uni')[1:]
    print(value)
    table_str = str(unicode_bit_to_vec(value)).replace('[','{').replace(']','}').replace(' ','')
    return table_str.replace("},{", '|').replace('{','').replace('}','')+'|'+str(origin_value)

app.run()
