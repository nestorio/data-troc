import os
import datetime
from flask import Flask, render_template, url_for, request, session, redirect, Markup, flash
import database.queries as query
import sys
sys.path.append("..")

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# This is the function that get called when a client wants to add a troc
def troquer():
    # We first check if there is an ongoing session
    status = 'client_Id' in session
    if(status == False):
        return redirect(url_for('login', next=request.url))

    # here if the add troc form has been submitted
    if request.method == 'POST':

        # here we check if a file has been submitted
        if 'image-file' in request.files:
            photo = request.files['image-file']
            dateTimeObj = datetime.datetime.now()
            timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H-%M-%S.%f)")
            photoname = photo.filename
            extension = os.path.splitext(photoname)[1]

            # here we are making sure that it was an image file that was submitted before uploading it to the database
            if(extension != ".jpg" and extension != ".png" and extension != ".jpeg" and extension != ".gif"):
                failMessage = "Invalid File Format "+ extension
                return render_template('troquer.html', username=session.get("first_name",None), failMessage = failMessage)

            # Here we want to create a string that will be the exact name of the file so we concatinate the date with name of the troc and the extension
            photofinalname = request.form['object-name'].replace(" ", "") + timestampStr.replace(" ", "") + extension

            if photo.filename != '':
                photo.save(os.path.join('./static/images/objets', photoname))
                old_file = os.path.join("./static/images/objets", photoname)
                new_file = os.path.join("./static/images/objets", photofinalname)
                os.rename(old_file, new_file)


            objectname = request.form['object-name']
            category = request.form['category']
            objectdescription = request.form['object-description']
            imagefile = photofinalname
            objectvalue = request.form['object-value']
            ville = request.form['ville']
            connectedUserEmail = session['email']

            query.addObject(objectname, objectdescription, objectvalue, category, imagefile, ville, True, connectedUserEmail)

            return "Thank you for adding your object"

    return render_template('troquer.html', username = session.get("first_name",None))