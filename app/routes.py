from flask import Flask                 # from the flask module import the Flask class

#OPP
app = Flask(__name__)                   # create an instance of Flask into the app
                                        # app now becomes an "object"

@app.get('/')                           # Flask decoreate to map routes to view functions
                                        # our function in flask is a view function
                                        # python dictionary .Dictionaries are key-value pairs.
def index():
    me ={
        "first_name": "Jason",
        "last_name": "Ramirez",
        "hobbies": "Playing video games",
        "is_active": True
    }
    return me

                            
                            # flask when you return a dictionary if all 
                            # #the fields are compatible with JSON, 
                            # it will be automatically converted into JSON for you.
