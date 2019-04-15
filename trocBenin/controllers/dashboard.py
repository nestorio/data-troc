from flask import Flask, render_template, url_for, request, session, redirect, Markup, flash
from database import queries as query

def dashboard():
    if ('client_Id' in session):
        trocs = query.searchIsTrocObjectforclient(session['email'])
        proposition = query.searchIsPropObjectforclient(session['email'])


        message = "You have " + str(len(trocs)) +" trocs"+" and " + str(len(proposition)) + " proposition"
        print(message)

        return render_template('dashboard.html', username = session.get("first_name",None), result = trocs, message=message, proposition=proposition)
    return redirect(url_for('login', next=request.url))
