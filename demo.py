from flask import Flask , redirect ,url_for , request ,render_template

app = Flask(__name__)

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

pd.options.display.max_rows = 9999

df = pd.read_csv('spam_ham_dataset.csv')
X = df['text']
y = df['label']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

vectorizer = CountVectorizer()

X_train_counts = vectorizer.fit_transform(X_train)

mdl = MultinomialNB()

mdl.fit(X_train_counts,y_train)

def pred(inp): 
    inp_counts = vectorizer.transform([inp])
    out = mdl.predict(inp_counts)[0]
    return out

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        user_inp = request.form['nm']
        return render_template('demo.html',res=pred(user_inp)) 
    else:
        return render_template('req.html')


if __name__  == '__main__':
    app.run()
