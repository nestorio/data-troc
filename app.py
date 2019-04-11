from flask import Flask, render_template, url_for, request, session, redirect, Markup, flash
from controllers import login, logout, index, apropos, contacter, trocs, register, dashboard
import sys
sys.path.append("..")
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#This is the route that leads to the index page
@app.route('/')
def index():
    return index.index()

@app.route('/')
def index():
    return index.index()

# This is the login route which links to the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    return login.login()

# This is the registration route which lead to the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    return register.register()

# This is the route for a propos
@app.route('/apropos')
def apropos():
    return apropos.apropos()

# This is the route for contact
@app.route('/contacter')
def contacter():
    return contacter.contacter()

# This si the toute for trocs
@app.route('/trocs')
def trocs():
    return trocs.trocs()

# This is the route for client dashboard
@app.route('/dashboard')
def dashboard():
    return dashboard.dashboard()

@app.route('/logout')
def logout():
    return logout.logout()

if __name__ == '__main__':
    app.run(debug=True)