from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/visualization')
def visualization():
    return render_template('visualization.html')

@app.route('/retraining')
def retraining():
    return render_template('retraining.html')

if __name__ == '__main__':
    app.run(debug=True)
