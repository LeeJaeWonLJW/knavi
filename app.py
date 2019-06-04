from flask import Flask, request
import predict_kw

app=Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello Python Flask</h1>"

@app.route("/cnn", methods = ['POST'])
def cnn():
    f = request.files['file']
    data = open(f, 'rb')
    print(data)
    return 'test'

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)
