Boilerplate for FLASK

This is boilerplate code for setting up user authentication via email confirmation for web app developement with Flask and SQLAlchemy. The DB is designed to hold only the basic user profiles (email, username password) so that the developer can use his/her own database of choise for the rest.

Bootstrap 4 is used to create a functional navbar and additional decorations are implemented through the provided css file. 

To run an app in Flask development server:

upgrade the database:
$ flask db upgrade

Set the environment variables:
$ export FLASK_APP=<name_of_the_app.py>
$ export SECRET_KEY='a secret key'created by:
>>> import secrets
>>> secrets.token_hex(16)

$ export SQLALCHEMY_DATABASE_URI='sqlite:///site.db' or the database URL
$ export MAIL_USERNAME='the username of the gmail of the admin'
$ export MAIL_PASSWORD='the password for the email'

To run in DEBUG mode (so that no need for restarting in every change):
$ export FLASK_DEBUG=1

To create a fresh the database:
>>> from app import db, create_app
>>> db.drop_all(app=create_app('default'))
>>> db.create_all(app=create_app('default'))

run the app:
$ flask run

test the app:
$ flask test

Please feel free to comment on further improvements /requests.

Sincerely,
Vayianos Pertsas
