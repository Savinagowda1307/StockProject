import pandas as pd
from flask import Flask, request, render_template
import joblib
from sklearn.tree import DecisionTreeClassifier
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/prediction1',methods=['POST','GET'])
def pred():
    a=[]
    if request.method=="POST":
        low = request.form['low']
        high = request.form['hi']
        volu = request.form['vl']
        a.extend([low,high,volu])
        model=joblib.load('stock.pkl')
        y_pred=model.predict([a])
        return render_template('prediction.html',msg="done",op=y_pred)
    return render_template('prediction.html')


if __name__ == '__main__':
    app.secret_key="savina"
    app.run(debug=True)



