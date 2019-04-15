from flask import Flask, render_template, url_for, request, session, redirect, Markup, flash
from database import queries as query

def objet(trocname):
    objets = query.searchIsTrocObject(all=True)
    objet = query.searchOneObject(imagename=trocname)
    proposals = query.proposalsForATroc(trocImage=trocname)
    owner = query.objectOwner(trocname)
    button = '<a href=' "/delete/"  + trocname + '><button style="background: transparent; border: solid 1px; border-radius: 2px; border-color: green; padding: 7px;">Supprimez objet</button></a>'
    if(len(objet) == 1):
        return render_template("single-object.html", objets=objets, objet=objet, owner=owner, button=button, proposals=proposals)
    return "The object you are looking for has been removed"

