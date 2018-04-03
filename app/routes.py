from flask import render_template
from app import app
<<<<<<< HEAD
from app.forms import LoginForm
=======
>>>>>>> 6fecdfa6a9a2fde248a3a3696bfeadfa558dd100
@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Niharika'}
    notifs = [
    	{
    		'author' : {'username':'Niharika'},
    		'body' : 'Selena Gomez is amazing!'
    	},
    	{
    		'author' : {'username' : 'Reena'},
    		'body' : '80!'
    	}
    ]
<<<<<<< HEAD
    return render_template('index.html',title='Home',user=user,notifs = notifs)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html',title='Sign In',form = form)
=======
    return render_template('index.html',title='Home',user=user,notifs = notifs)
>>>>>>> 6fecdfa6a9a2fde248a3a3696bfeadfa558dd100
