


from flask import Flask, render_template, url_for, request, session, redirect, Markup, flash
import sys
sys.path.append("..")
import clientQueries

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
    if('client_Id' in session):
        return redirect(url_for('dashboard'))
    return render_template('index.html')

# This is the login route which links to the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if ('client_Id' in session):
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        clientData = clientQueries.loginUser(request.form['username'], request.form['password'])
        if(clientData['client_Id'] == ""):
            errorMessage = "Invalid email or password"
            return render_template('login.html', show = errorMessage)
        session['first_name'] = clientData['first_name']
        session['client_Id'] = clientData['client_Id']
        return redirect(url_for('dashboard'))
    return render_template('login.html')

# This is the registration route which lead to the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userData = {
            "lastname": request.form['lastname'],
            "firstname": request.form['firstname'],
            "address": request.form['address'],
            "telephone": request.form['telephone'],
            "password": request.form['password'],
            "email": request.form['email'],
            "message": Markup('<strong>You already have an account. <a href="login">Click here to login</a></strong>')
        }
        if(clientQueries.userExist(userData['email'])):
            return render_template('sign-up.html', lastname = userData['lastname'], firstname = userData['firstname'], address = userData['address'], telephone = userData['telephone'], password = userData['password'], email = userData['email'], message = userData['message'])
        if(clientQueries.registerClient(userData)):
            return Markup('<strong>Thank you for registering. <a href="login">Click here to login</a></strong>')

    return render_template('sign-up.html')

# This is the route for a propos
@app.route('/apropos')
def apropos():
    return "No template yet"

# This is the route for contact
@app.route('/contacter')
def contacter():
    return "No template yet"

# This si the toute for trocs
@app.route('/trocs')
def trocs():
    return render_template('trocs.html')

# This is the route for client dashboard

@app.route('/dashboard')
def dashboard():
    if ('client_Id' in session):
        return render_template('dashboard.html')
    return redirect(url_for('login', next=request.url))

@app.route('/logout')
def logout():
    session.pop('client_Id', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
