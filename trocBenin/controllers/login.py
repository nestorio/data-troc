from flask import Flask, render_template, url_for, request, session, redirect, Markup, flash
import database.queries as dbqueries

def login():
    if ('client_Id' in session):
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        clientData = dbqueries.loginUser(request.form['username'], request.form['password'])
        if(clientData['client_Id'] == ""):
            errorMessage = "Invalid email or password"
            return render_template('login.html', show = errorMessage)
        session['first_name'] = clientData['first_name']
        session['client_Id'] = clientData['client_Id']
        session['email'] = clientData['email']
        session['last-name']=clientData['last-name']
        return redirect(url_for('dashboard'))
    return render_template('login.html')