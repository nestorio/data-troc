from flask import Flask, render_template, url_for, request, session, redirect, Markup, flash

def contacter():
    return render_template('contact.html')