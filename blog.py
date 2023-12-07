from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello this is abhinand, World!</p>"
@app.route("/about")
def about():
    return "<p>This is the about page i have in my application!</p>"

if __name__ == '__main__':
        app.run(debug=True) 
