from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/postrequest')
def post_req():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
