import flask 
import flask_sqlalchemy
import flask_restless
import os

app = flask.Flask(__name__, static_url_path="")
app.config['DEBUG'] = True
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = flask_sqlalchemy.SQLAlchemy(app)

@app.route('/')
def main():
    return flask.render_template('index.html')

@app.route('/templates/<path:path>')
def send_all(path):
    return flask.send_from_directory('templates', path)

class Park(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    park_name = db.Column(db.Unicode)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.Unicode)

class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    program_name = db.Column(db.Unicode)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.Unicode)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Unicode)

class PostedMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Unicode)
    user_id = db.Column(db.Integer)
    activity_id = db.Column(db.Integer)
    park_id = db.Column(db.Integer)
    posted_on = db.Column(db.DateTime)
   
class PostedResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    response = db.Column(db.Unicode)
    message_id = db.Column(db.Integer)
    responded_on = db.Column(db.DateTime)




# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Unicode, unique=True)
#     birth_date = db.Column(db.Date)


# class Computer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Unicode, unique=True)
#     vendor = db.Column(db.Unicode)
#     purchase_time = db.Column(db.DateTime)
#     owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
#     owner = db.relationship('Person', backref=db.backref('computers',
#                                                          lazy='dynamic'))



# Create the database tables.
db.create_all()





# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.

# manager.create_api(Person, methods=['GET', 'POST', 'PUT', 'DELETE'])
# manager.create_api(Computer, methods=['GET'])

manager.create_api(Park, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(Activity, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(Resource, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(Program, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(User, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(PostedMessage, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(PostedResponse, methods=['GET', 'POST', 'PUT', 'DELETE'])


# db.session.add(User(user_name="John J"))
# db.session.add(User(user_name="Jessie"))
# db.session.add(User(user_name="John L"))
# db.session.add(User(user_name="Brandon"))
# db.session.add(User(user_name="Jamie"))
# db.session.add(Park(park_name="Stewart Heights"))
# db.session.add(Activity(activity_name="Skateboarding"))
# db.session.add(Resource(resource_name="Court"))
# db.session.commit()

# start the flask loop
app.run()
