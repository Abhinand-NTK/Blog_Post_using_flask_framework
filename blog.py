from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template('home.html')
@app.route("/about")
def about():
    return "<p>This is the about page i have in my application!</p>"

if __name__ == '__main__':
        app.run(debug=True) 
