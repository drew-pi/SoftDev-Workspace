from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request, session, redirect, url_for

app = Flask(__name__)    #create Flask object

app.secret_key = 'hi'
usernames=['yee', 'ah']
passwords = ['goofy', 'ah']

@app.route('/')
def index():
    if 'username' in session and 'password' in session:
        if session['username'] in usernames:
            if passwords[usernames.index(session['username'])] == session['password']:
                curr_usr = session['username']
                print(curr_usr)
                return render_template('response.html', username=curr_usr)
    return redirect(url_for('relogin'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/relogin', methods=['GET', 'POST'])
def relogin():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    return render_template('relogin.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('password', None)
    print(session)
    return redirect(url_for('index'))
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()