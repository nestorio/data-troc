from flask import Flask, render_template, url_for, request, session, redirect, Markup, flash

def logout():
    session.pop('client_Id', None)
    return redirect(url_for('index'))