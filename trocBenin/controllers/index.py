from flask import Flask, render_template, url_for, request, session, redirect, Markup, flash
from database import queries as query
def index():
    if('client_Id' in session):
        return redirect(url_for('dashboard'))
    objets = query.searchIsTrocObject(all=True)
    categories = [
        {'vehicule': len(query.searchIsTrocObject(category="vehicule"))},
        {'electronique': len(query.searchIsTrocObject(category="electronique"))},
        {'immobilier': len(query.searchIsTrocObject(category="immobilier"))},
        {'vetements': len(query.searchIsTrocObject(category="vetements"))},
        {'animaldecompagnie': len(query.searchIsTrocObject(category="animaldecompagnie"))},
        {'outil': len(query.searchIsTrocObject(category="outil"))}

    ]
    return render_template('index.html', objets =  objets, categories = categories)