from flask import Flask, render_template, request, redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import string
import random

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

urls = {}

def short_url_gen():
    length = 6
    while True: 
        short_code = "".join(random.choices(string.ascii_letters, k=length))
        if short_code not in urls:
            return short_code
    

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_url = request.form['input_url']
        result = short_url_gen()
        for key, value in urls.items():
            if input_url == value:
                return render_template('index.html', result=key) 
        urls[result] = input_url
        return render_template('index.html', result=result)
    else:
        return render_template('index.html')

@app.route('/<short_code>')
def redirect_url(short_code):
    if short_code in urls:
        return redirect(f'{urls[short_code]}')
    else:
        return render_template('index.html', result="No result found")

if __name__ == "__main__":
    app.run(debug=True)