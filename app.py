from flask import Flask, request, jsonify, render_template
from werkzeug import secure_filename

import predict_kw

app=Flask(__name__)

@app.route("/cnn", methods = ['POST'])
def cnn():
    f = request.files['file']
    data = f.read()
    name, score = predict_kw.getScore(data)
    sort_score = sorted(score)
    result=None
    for i in range(0, len(score), 1):
        if score[i] == sort_score[len(sort_score)-1]:
            result = (name[i], score[i])
            break
    response = {
        "name": result[0]
    }
    
    return jsonify(response), 200

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)
