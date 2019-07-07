from flask import Flask
from flask import render_template,redirect,request
from flask import session,flash,jsonify
app = Flask(__name__)

app.secret_key = "somesupersecretkey"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    return jsonify({'message':'thanks for submitting'})


if __name__ == '__main__':
    app.run(debug=True) # false when submitting