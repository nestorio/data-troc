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
