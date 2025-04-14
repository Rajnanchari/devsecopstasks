# -*- coding: utf-8 -*-
"""
@author: Amisha
"""

from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def generate_random_number():
    global num
    num = np.random.randint(1,100)
    print("Random Number Generated:",num)    

# root route
@app.route('/')
def welcome_page():
    global num
    generate_random_number()
    return render_template('number_game.html',num = num, res = "noinput")

# guess route
@app.route('/guess', methods = ['POST'])
def user_guess():
    guess = int(request.form['guess'])
    if(guess == num):
        return render_template('number_game.html',num = num, res = 'correct')
    elif(guess>num):
        return render_template('number_game.html',res = 'high', num = num)
    elif(guess<num):
        return render_template('number_game.html',res = 'low', num = num)
    else:
        return render_template('number_game.html',res = 'noinput', num = num)

if __name__ == '__main__':
    app.run(debug=True)