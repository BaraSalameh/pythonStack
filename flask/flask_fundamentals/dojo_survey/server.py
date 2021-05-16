from flask import Flask,render_template,redirect,request,session
from flask.signals import template_rendered
app = Flask(__name__)
app.secret_key = "i'am secret"
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result',methods=['POST','GET'])
def result():
    session['name'] = request.form['name']
    session['dojo-location'] = request.form['dojo-location']
    session['favorite-language'] = request.form['favorite-language']
    session['comment'] = request.form['comment']

    return redirect('/show')

@app.route('/show')
def show():
    return render_template('show.html')

if __name__ == '__main__':
    app.run(debug=True)