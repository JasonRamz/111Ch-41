#!/usr/bin/env python3
#-#- coding: utf-8 -#-
"""Sample hello world from flask"""

from flask import Flask


app = Flask(__name__)

@app.route('/')                           # Flask decoreate to map routes to view functions

def main():
    return "Dr.Rafael is the best!!!"


@app.route('/aboutme')                           # Flask decoreate to map routes to view functions
                                        # our function in flask is a view function
                                        # python dictionary .Dictionaries are key-value pairs.
def intro():
    me =["First Name: Jason Ramirez", "Last Name: Ramirez", "Hobbies:  Playing video games", "is_active: True"]
    bullet_list = "".join(
        "<li>%s</li>" %intro for intro in me
    )
    return "<ul>%s</ul>" % bullet_list

                            
                            # flask when you return a dictionary if all 
                            # #the fields are compatible with JSON, 
                            # it will be automatically converted into JSON for you.