# Andrew Piatetsky (BBAY)
# SoftDev
# K10 -- flask-jinja
# 2022-10-13
# time spent: 30 mins

# DEMO 
# basics of /static folder

from flask import Flask
app = Flask(__name__) 

@app.route("/") # this is the root route    
def hello_world(): 
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
