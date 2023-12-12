from flask import Flask,render_template
from forms import RegistrationFrom,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '15d8129dff01afe80571f3f3995627f0'


posts = [
     
     {
          'author':'Abhinand',
          'title':"Blog Post 1",
          'content':"First Post Content",
          'date_posted':'April 21 ,2018',
     },
     {
          'author':'Anandu Vijay',
          'title':"Blog Post 2",
          'content':"Second Post Content",
          'date_posted':'April 23,2018',
     }
]
@app.route("/")
def Home():
    return render_template('home.html',posts = posts)
@app.route("/about")
def about():
    return "<p>This is the about page i have in my application!</p>"

@app.route("/register")
def register():
     form = RegistrationFrom()
     return render_template('register.html',title='Register',form=form)

@app.route("/login")
def login():
     form = LoginForm()
     return render_template('login.html',title='Login',form=form)


if __name__ == '__main__':
        app.run(debug=True) 
