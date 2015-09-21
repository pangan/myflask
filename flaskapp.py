import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

'''from functools import wraps'''

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')


'''
def check_auth(username, password):
	logins = dict()

	try:
		with open(CONFIG_FOLDER+'/logins.json') as json_logins:
			logins = json.load(json_logins)
			json_logins.close()
	except Exception, e:
		return False
	
	if username in logins:
		return logins[username] == password
	return False	
	

def authenticate():
	return ('Bad Login! you are not allowed to use this system!',
	 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

def requires_auth(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if not auth or not check_auth(auth.username, auth.password):
			return authenticate()
		return f(*args, **kwargs)
	return decorated

'''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"


@app.route('/logout')
def logout():
	return render_template('logout.html'), 401

'''
@app.route('/admin')
@requires_auth
def logout():
	return render_template('admin.html')
'''

if __name__ == '__main__':
    app.run()

