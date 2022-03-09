from flask import *  

app  = Flask(__name__)

@app.route('/')  
def home():
    return "Hello BorntoDev2!!"  

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
