from flask import *  

app  = Flask(__name__)

@app.route('/')  
def home():
    return "Hello BorntoDev2!!"  

if __name__ == '__main__':
