from flask import Flask,render_template,request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/reg',methods = ['POST','GET'])
def reg():
    if request.method == 'POST':
        reg = request.form.get('regex')
        text = request.form.get('text')
        matches  = re.findall(reg,text)
        return render_template('result.html',matches = matches)
    return render_template('home.html')
    
if __name__ == '__main__':
    app.run(debug=True)
