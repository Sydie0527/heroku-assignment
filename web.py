from Flask import Flask
app = Flask(__name__)

@app.route('/')
def index();
 return 'Name: Morgia, Lord Sydreck  Age: 20  Course&Year: BSIT 2'
