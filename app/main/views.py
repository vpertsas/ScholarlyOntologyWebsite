from flask import render_template, request, redirect, url_for
from . import main
from flask_login import current_user

@main.route('/')
def index():
    return render_template('index.html')


@main.route("/about")
def about():
    return render_template('about.html')


@main.route("/ScholarlyOntology")
def ScholarlyOntology():
    return render_template('ScholarlyOntology.html')


@main.route("/events")
def events():
    return render_template('events.html')


@main.route("/ActivityTypes")
def ActivityTypes():
    return render_template('ActivityTypes.html')


@main.route("/ResearchSpotlight")
def ResearchSpotlight():
    return render_template('ResearchSpotlight.html')


@main.route("/resources")
def resources():
    if current_user.is_authenticated:
        return render_template('resources.html')
    return redirect(url_for('auth.register'))


@main.route("/references")
def references():
    return render_template('references.html')


@main.route("/NeMO")
def NeMO():
    return render_template('NeMO.html')
