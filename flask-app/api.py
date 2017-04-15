import flask 
import flask.ext.sqlalchemy
import flask.ext.restless
import os

# Create the Flask application and the Flask-SQLAlchemy object.
app = flask.Flask(__name__, static_url_path="")
app.config['DEBUG'] = True
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
db = flask.ext.sqlalchemy.SQLAlchemy(app)

@app.route('/')
def main():
    return flask.render_template('index.html')



# Create your Flask-SQLALchemy models as usual but with the following two
# (reasonable) restrictions:
#   1. They must have a primary key column of type sqlalchemy.Integer or
#      type sqlalchemy.Unicode.
#   2. They must have an __init__ method which accepts keyword arguments for
#      all columns (the constructor in flask.ext.sqlalchemy.SQLAlchemy.Model
#      supplies such a method, so you don't need to declare a new one).
class Park(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    park_name = db.Column(db.Unicode)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    park_name = db.Column(db.Unicode)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.Unicode)

class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    program_name = db.Column(db.Unicode)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Unicode)

# class PostedMessage(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     message = db.Column(db.Unicode)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
#     park_id = db.Column(db.Integer, db.ForeignKey('park.id'))
#     posted_on = db.Column(db.DateTime)
#     user = db.relationship('User', backref=db.backref('user',
#                                                          lazy='dynamic'))
#     activity = db.relationship('Activity', backref=db.backref('activity',
#                                                          lazy='dynamic'))
#     park = db.relationship('Park', backref=db.backref('park',
#                                                          lazy='dynamic'))

# class PostedResponse(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     response = db.Column(db.Unicode)
#     message_id = db.Column(db.Integer, db.ForeignKey('message.id'))
#     responded_on = db.Column(db.DateTime)
#     message_responded_to = db.relationship('PostedMessage', backref=db.backref('postedmessage',
#                                                          lazy='dynamic'))

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    birth_date = db.Column(db.Date)


class Computer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    vendor = db.Column(db.Unicode)
    purchase_time = db.Column(db.DateTime)
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    owner = db.relationship('Person', backref=db.backref('computers',
                                                         lazy='dynamic'))


# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Person, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Computer, methods=['GET'])

# start the flask loop
app.run()
