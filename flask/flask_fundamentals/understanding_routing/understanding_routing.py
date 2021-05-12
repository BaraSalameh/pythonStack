from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<something>')
def say_something(something):
    return "Hi "+something

@app.route('/repeat/<count>/<thing>')
def repeat(count,thing):
    return thing*int(count)

if __name__ == "__main__":
    app.run(debug=True)