from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('waveletsUsefulDescription.html')


@app.route('/morlet')
def morletWavelet():
    return render_template('morlet.html')

@app.route('/haar')
def haarWavelet():
    return render_template('haar.html')

@app.route('/mexicanHat')
def mexHatWavelet():
    return render_template('mexicanHat.html')

@app.route('/daubechie')
def daubechieWavelet():
    return render_template('daubechie.html')

@app.route('/complexWavelets')
def complexWavelet():
    return render_template('complexWavelets.html')

@app.route('/waveletTransform')
def waveletTransform():
    return render_template('waveletTransform.html')

if __name__ == '__main__':
    app.run(debug=True)