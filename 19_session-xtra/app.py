'''
<AKA Wolfgang>
Andrew, Kosta, Aaron Gersh
SoftDev
K19 -- Session/Cookies/Logging in and out
2022-11-6
1.5 hours

DISCO:

My browser can block cookies but cannot remove them, the cookie still exists but for some reason the server cannot read it

in this iteration, you can have an already existing cookie without a password, it will log you in

redirect_url directs the user to the given route

url_for allows you to input the function name instead of the route definition

QCC:

How can you store the secret key secretly (not in the python file or sql database)

what other ways can cookies be used (this cookie is called 'session' what other flask specific cookies are there)
'''


from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request, session, redirect

app = Flask(__name__)    #create Flask object

# hard coded passwords and secret keys (not so secret)
app.secret_key = 'hi'
username = 'yee'
password = 'goofy'


@app.route('/')
def index():
    print(session) # print the cookie dictionary like object
    if 'username' in session:
        return render_template('response.html',username=session['username'])
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = '' # shows what went wrong with usr pwd combo
    if request.method == 'POST':
        input_usrname = request.form['username']
        input_pwd = request.form['password']
        if input_usrname == username and input_pwd == password:
            session['username'] = input_usrname
            session['password'] = input_pwd
            return redirect('/')
        else:
            msg = 'wrong password bud'

    return render_template('login.html',fail_login = msg)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None) # logs the user out by deleting the cookie for username and pwd
    session.pop('password', None)
    print(session) # print the cookie dictionary like object
    return redirect('/')
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()