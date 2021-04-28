from flask import Flask, render_template
from flask_cors import CORS
from .config  import init_db, init_graphql

app = Flask(__name__)
app.secret_key = b')\xa4\xdd\x88~\xa5F\xd0\xf1\x12\x80i>bm\x9d'
CORS(app)

init_db()

@app.route('/')
def welcome():
    return render_template('index.html')

init_graphql(app)
