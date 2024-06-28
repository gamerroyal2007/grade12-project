from flask import Blueprint, render_template

views = Blueprint('views',__name__)

@views.route('/') #decorator: basically ; function_a = function_b(function_a) where function_b rewrites function_a a decorator is denoted with "@"
def home(): 
   return render_template("home.html")


