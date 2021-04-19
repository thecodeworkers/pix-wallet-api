from flask import Flask, render_template
from flask_cors import CORS
from .config  import init_db, init_graphql

app = Flask(__name__)
app.secret_key = b'\x9b\x0f\xe7\xc6\xdcJu\xb5\xeb\xaf\xbft\x1d\xed\x98@'
CORS(app)

init_db()

@app.route('/')
def welcome():
    return render_template('index.html')

init_graphql(app)
