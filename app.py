from flask import Flask,render_template
# from flask_bootstrap import Bootstrap
from data import Articles
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import InputRequired,Email,Length

app=Flask(__name__)
app.config['SECRET_KEY']='Thisissupposedtobesecret!'
# Bootstrap(app)
Articles=Articles()

class LoginForm(FlaskForm):
    username=StringField('username',validators=[InputRequired(),Length(min=4,max=15)])
    password=PasswordField('password',validators=[InputRequired(),Length(min=8,max=80)])
    remember=BooleanField('remember me')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html',articles=Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html',id=id)

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',form=form)    

if __name__=='__main__': 
    app.run(debug=True)