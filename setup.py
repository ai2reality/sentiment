import numpy
from flask import Flask, render_template,redirect,request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from Form import LoginForm
from flask_wtf.csrf import CSRFProtect

'''tokenize sentance


     for k in sorted(ss):
         print('{0}: {1}, '.format(k, ss[k]), end='')
     print()
'''
app = Flask(__name__)
app.secret_key = 'random#string'
@app.route('/')
def name():
    p=[]
    return render_template('index.html',ss=p)

@app.route('/index',methods=['GET','POST'])
def hello_name():
    if request.method == 'POST':
      paragraph = request.form["texts"]
      lines_list = tokenize.sent_tokenize(paragraph)

      sid = SentimentIntensityAnalyzer()
      for sentence in lines_list:
           print(sentence)
           ss = sid.polarity_scores(sentence)
    return render_template("test.html",ss = ss)


if __name__ == '__main__':
   app.run(debug = True)
