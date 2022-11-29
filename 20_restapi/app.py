'''
TNPG: burriot (Andrew, Raven,Ayman)
SoftDev
K20 - A RESTful Journey Skyward/REST API/Called a nasa api to display an image and blurb
2022-11-21
time:20min
'''



from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
import requests

app = Flask(__name__)    #create Flask object

# finds the api key in the dedicated file
api_key = open(r"key_nasa","r").read()
api_query = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

def get_data():
    response = requests.get(api_query) # response object
    print(response) # prints a response code (either 200 or something else)
    data = response.json() # converts the response object into a dictionary or serialized object
    return data



@app.route("/")
def main():
    data = get_data() # dictionary (or other similar) form
    title = data['title']
    blurb = data['explanation']
    photo_url = data['url']

    return render_template("main.html",title=title,img_url=photo_url,blurb=blurb)


if __name__ == "__main__":
    app.debug = True 
    app.run()
