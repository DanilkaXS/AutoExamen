from pprint import pprint

from flask import Flask, render_template, url_for, request
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/postrequest', methods=['POST'])
def post_req():
    data = json.loads(request.data)
    pprint(data)
    return '200'


if __name__ == '__main__':
    app.run()
