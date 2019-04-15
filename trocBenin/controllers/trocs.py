from flask import Flask, render_template, url_for, request, session, redirect, Markup, flash
from database import queries as query

def trocs():
    objets = query.searchIsTrocObject(all=True)
    length = len(objets)
    if request.method == 'POST':
        searchquery = request.form['searchquery']
        category = request.form['category']
        town = request.form['town']
        print("search query is: "+ searchquery + " catergory is: " + category + " town is: " + town)

        if(category == "" and town == ""):

            return render_template('trocs.html', result = objets, objets = objets, length = length)
        if(category != "" and town != ""):
            result = query.searchIsTrocObject(category=category, ville=town)
            length = len(result)
            return render_template('trocs.html', result=result, objets=objets, length = length)
        if(category != "" and town == ""):
            result = query.searchIsTrocObject(category=category)
            length = len(result)
            return render_template('trocs.html', result=result, objets=objets, length = length)
        if (category == "" and town != ""):
            result = query.searchIsTrocObject(ville=town)
            length = len(result)
            return render_template('trocs.html', result=result, objets=objets, length = length)

        return render_template('trocs.html', result = objets, objets = objets, length = length)

    return render_template('trocs.html', result = objets, objets = objets, length = length)