from flask import Flask, render_template, url_for, request, session, redirect, Markup, flash
from database import queries as query

def objet(trocname):
    objets = query.searchIsTrocObject(all=True)
    objet = query.searchOneObject(imagename=trocname)
    owner = query.objectOwner(trocname)
    if(len(objet) == 1):
        return render_template("single-object.html", objets=objets, objet=objet, owner=owner)
    return "The object you are looking for has been removed"

