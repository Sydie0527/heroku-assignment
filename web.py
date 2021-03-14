from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
 return 'Morgia, Lord Sydreck BSIT 2'
