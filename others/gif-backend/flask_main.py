from flask import Flask, request

app = Flask(__name__)

@app.route("/swgif")
def get_gif():
    origin_value = request.args.get("gif") or ''
    return open(f'gif/{origin_value}.vm', 'r').read().replace('\n', '')

app.run()
