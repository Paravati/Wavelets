from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('waveletsUsefulDescription.html')


@app.route('/morlet')
def morletWavelet():
    return render_template('morlet.html')


if __name__ == '__main__':
    app.run(debug=True)