from flask import *  

app  = Flask(__name__)

@app.route('/')  
def home():
    return "Hello BorntoDev!!"  

if __name__ == '__main__':
   app.run()
