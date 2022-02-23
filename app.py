from flask import Flask, render_template, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import string
import random

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def short_url_gen():
    length = 6
    short_code = "".join(random.choices(string.ascii_letters, k=length))
    return short_code

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_url = request.form['input_url']
        result = short_url_gen()
        return render_template('index.html', result=result)
    else:
        return render_template('index.html')

@app.route('/<short_code>')
def redirect():
    SELECT long_url FROM URL WHERE short_url = short_code

if __name__ == "__main__":
    app.run(debug=True)