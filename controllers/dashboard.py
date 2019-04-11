def dashboard():
    if ('client_Id' in session):
        return render_template('dashboard.html')
    return redirect(url_for('login', next=request.url))
