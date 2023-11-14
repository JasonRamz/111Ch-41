#!/usr/bin/env python3
#-#- coding: utf-8 -#-
"""Sample hello world from flask"""

from flask import Flask


app = Flask(__name__)

@app.get('/')                           # Flask decoreate to map routes to view functions

def main():
    return "Dr.Rafael is the best!!!"


@app.get('/aboutme')                           # Flask decoreate to map routes to view functions
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