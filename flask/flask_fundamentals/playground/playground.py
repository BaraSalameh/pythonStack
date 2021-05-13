from flask import Flask,render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('play.html',time = 0)

@app.route('/play/<times>')
def play_times(times):
    return render_template('play.html',time = int(times))

@app.route('/play/<times>/<colors>')
def play_times_color(times,colors):
    print(colors)
    return render_template('play_color.html',time = int(times) , color = colors)

if __name__ == "__main__":
    app.run(debug=True)

