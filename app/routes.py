from app import app
from flask import render_template, url_for, redirect, flash, request, session


@app.route("/")
def home():
    return { "route": '/', "message": 'You are home'}