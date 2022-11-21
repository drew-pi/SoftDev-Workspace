from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating

app = Flask(__name__)    #create Flask object




@app.route("/")
def main():
    return "hello world"



if __name__ == "__main__":
    app.debug = True 
    app.run()
