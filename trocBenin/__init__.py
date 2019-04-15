

from flask import Flask, render_template, url_for, request, session, redirect, Markup, flash
from controllers import login as log, logout as logo, index as inde, apropos as aprop, contacter as contac, trocs as troc, register as regist, dashboard as dashb, troquer as troq, objet as obj, proptroc as prop, managetroc as managt
import database.queries as dbqueries

import sys
sys.path.append("..")



#import pymongo
#from flask_jwt_extended import JWTmanager
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#app.config['MONGO_URI'] = 'mongodb://charly:Gobem1996.@trocbenin-shard-00-00-diyz7.mongodb.net:27017,trocbenin-shard-00-01-diyz7.mongodb.net:27017,trocbenin-shard-00-02-diyz7.mongodb.net:27017/test?ssl=true&replicaSet=TrocBenin-shard-0&authSource=admin&retryWrites=true'
#mongo = PyMongo(app)
#client = pymongo.MongoClient("mongodb://charly:Gobem1996.@trocbenin-shard-00-00-diyz7.mongodb.net:27017,trocbenin-shard-00-01-diyz7.mongodb.net:27017,trocbenin-shard-00-02-diyz7.mongodb.net:27017/test?ssl=true&replicaSet=TrocBenin-shard-0&authSource=admin&retryWrites=true")
#db = client.test



#This is the route that leads to the index page
@app.route('/')
def index():
    return inde.index()

# This is the login route which links to the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    return log.login()

# This is the registration route which lead to the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    return regist.register()

# This is the route for a propos
@app.route('/apropos')
def apropos():
    return aprop.apropos()

# This is the route for contact
@app.route('/contacter')
def contacter():
    return contac.contacter()


# This is the route for a client to see all his troc
@app.route('/trocs', methods=['GET', 'POST'])
def trocs():
    return troc.trocs()

# This is the route that leads you to a particular object
@app.route('/trocs/<trocname>')
def objet(trocname):
    return obj.objet(trocname)

@app.route('/proposertroc/<trocname>', methods=['GET', 'POST'])
def propobjet(trocname):
    return prop.propobjet(trocname)

# this is the route for a client to add a troc
@app.route('/troquer', methods=['GET', 'POST'])
def troquer():
    return troq.troquer()


# This is the route for client dashboard

@app.route('/dashboard')
def dashboard():
    return dashb.dashboard()

@app.route('/logout')
def logout():
    return logo.logout()

@app.route('/managetroc/<trocname>')
def managetroc(trocname, methods=['GET', 'POST']):
    return managt.objet(trocname)

if __name__ == '__main__':
    app.run(debug=True)

