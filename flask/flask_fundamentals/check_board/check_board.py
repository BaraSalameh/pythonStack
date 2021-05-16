from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def firstQ():
    return render_template('index.html',rows = 0, cols = 0)

@app.route('/<x>')
def secondQ(x):
    return render_template('index.html',rows = int(x), cols= 0)

@app.route('/<x>/<y>')
def thirdQ(x,y):
    return render_template('index.html',rows = int(x), cols = int(y))
    
@app.route('/<x>/<y>/<color1>/<color2>')
def fourthQ(x,y,color1,color2):
    return render_template('index.html',rows = int(x), cols = int(y),first_color=color1,second_color = color2)
    
if __name__ == '__main__':
    app.run(debug=True)