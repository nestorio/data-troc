def logout():
    session.pop('client_Id', None)
    return redirect(url_for('index'))