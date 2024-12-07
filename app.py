from flask import Flask, render_template
from flask_cors import CORS  # Import the CORS middleware for Flask

app = Flask(__name__)

# Define the allowed origins
origins = [
    "http://localhost:8000",
    "http://localhost",
    "http://127.0.0.1:5000",  # Local development
    "https://pipeline-frontend-summative.onrender.com",  # Frontend URL
    "https://pipeline-summative-3.onrender.com",  # API URL
]

# Apply CORS only to specific routes
CORS(app, resources={
    r"/prediction": {"origins": origins},
    r"/visualization": {"origins": origins},
    r"/retraining": {"origins": origins}
}, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

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
    app.run(debug=True, host='0.0.0.0', port=5000)
