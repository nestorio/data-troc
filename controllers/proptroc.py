from flask import Flask, render_template, url_for, request, session, redirect, Markup, flash
from database import queries as query
import datetime
import os
import sys
sys.path.append("..")

def propobjet(imagename: str=""):
    if ('client_Id' in session):
        obj = query.searchIsTrocObject(all=True)
        objectOwner = query.objectOwner(imagename=imagename)
        print("document is: ")
        print(objectOwner)
        if(session['email'] == objectOwner):

            return("You cannot exchange this object because it belongs to you")
        if request.method == 'POST':

            # here we check if a file has been submitted
            if 'image-file' in request.files:
                photo = request.files['image-file']
                dateTimeObj = datetime.datetime.now()
                timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H-%M-%S.%f)")
                photoname = photo.filename
                extension = os.path.splitext(photoname)[1]

                # here we are making sure that it was an image file that was submitted before uploading it to the database
                if (extension != ".jpg" and extension != ".png" and extension != ".jpeg" and extension != ".gif"):
                    failMessage = "Invalid File Format " + extension
                    return render_template('troquer.html', username=session.get("first_name", None),
                                           failMessage=failMessage)

                # Here we want to create a string that will be the exact name of the file so we concatinate the date with name of the troc and the extension
                photofinalname = request.form['object-name'].replace(" ", "") + timestampStr.replace(" ",
                                                                                                     "") + extension

                if photo.filename != '':
                    photo.save(os.path.join('./static/images/objets', photoname))
                    old_file = os.path.join("./static/images/objets", photoname)
                    new_file = os.path.join("./static/images/objets", photofinalname)
                    os.rename(old_file, new_file)

                objectname = request.form['object-name']
                trocob  = request.form['troc-image']
                category = request.form['category']
                objectdescription = request.form['object-description']
                imagefile = photofinalname
                objectvalue = request.form['object-value']
                ville = request.form['ville']
                connectedUserEmail = session['email']

                query.addProposal(objectname, objectdescription, objectvalue, category, imagefile, ville, False,
                                connectedUserEmail, trocob)

                return "Thank you for adding your proposal"

        return render_template('propTroc.html', imagename=imagename, isTroc=True, objets=obj)
    message = "Vous devez " + "<a href='/login'>" + "vous connecter" + "</a>" + " pour continuer. Si vous n'avez pas de compte, " + "<a href='/register'>cliquez ici</a> pour vous inscrire"
    return(message)