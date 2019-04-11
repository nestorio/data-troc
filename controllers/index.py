def index():
    if('client_Id' in session):
        return redirect(url_for('dashboard'))
    return render_template('index.html')