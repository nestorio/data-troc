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