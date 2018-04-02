from flask import render_template
from app import app
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
    return render_template('index.html',title='Home',user=user,notifs = notifs)