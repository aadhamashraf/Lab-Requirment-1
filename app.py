# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form.get('name')
    age = request.form.get('age')
    
    return render_template('result.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
