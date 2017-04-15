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

class ResourceActivities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer)
    activity_id = db.Column(db.Integer)
   
class PostedResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    response = db.Column(db.Unicode)
    message_id = db.Column(db.Integer)
    responded_on = db.Column(db.DateTime)

class UserActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    activity_id = db.Column(db.Integer)

class UserPark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    park_id = db.Column(db.Integer)
    
class ParkActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    park_id = db.Column(db.Integer)
    activity_id = db.Column(db.Integer)



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
manager.create_api(Park, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(Activity, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(Resource, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(Program, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(User, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(PostedMessage, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(PostedResponse, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(UserActivity,methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(UserPark, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(ParkActivity, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(ResourceActivities, methods=['GET', 'POST', 'PUT', 'DELETE'])

# Add some data to your endpoints
db.session.add(User(user_name="John J"))
db.session.add(User(user_name="Jessie"))
db.session.add(User(user_name="John L"))
db.session.add(User(user_name="Brandon"))
db.session.add(User(user_name="Jamie"))

db.session.add(Park(park_name="Stewart Heights"))
db.session.add(Park(park_name="Manitou"))
db.session.add(Park(park_name="Alder"))
db.session.add(Park(park_name="Wright"))
db.session.add(Park(park_name="Point Defiance"))

db.session.add(UserPark(user_id=1, park_id=1))
db.session.add(UserPark(user_id=3, park_id=2))
db.session.add(UserPark(user_id=5, park_id=2))

db.session.add(Activity(activity_name="Skateboarding"))
db.session.add(Activity(activity_name="Basketball"))
db.session.add(Activity(activity_name="Bocce Ball (Lawn Bowling)"))
db.session.add(Activity(activity_name="Tennis"))
db.session.add(Activity(activity_name="Swimming"))
db.session.add(Activity(activity_name="Hiking"))
db.session.add(Activity(activity_name="Baseball"))
db.session.add(Activity(activity_name="Softball"))
db.session.add(Activity(activity_name="Water Polo"))

db.session.add(ResourceActivities(resource_id=1, activity_id=2))
db.session.add(ResourceActivities(resource_id=2, activity_id=3))
db.session.add(ResourceActivities(resource_id=3, activity_id=5))
db.session.add(ResourceActivities(resource_id=3, activity_id=9))

db.session.add(UserActivity(user_id=2, activity_id=1))
db.session.add(UserActivity(user_id=3, activity_id=2))
db.session.add(UserActivity(user_id=4, activity_id=2))

db.session.add(ParkActivity(park_id=1, activity_id=1))
db.session.add(ParkActivity(park_id=1, activity_id=4))
db.session.add(ParkActivity(park_id=2, activity_id=2))
db.session.add(ParkActivity(park_id=2, activity_id=4))
db.session.add(ParkActivity(park_id=2, activity_id=3))
db.session.add(ParkActivity(park_id=2, activity_id=6))
db.session.add(ParkActivity(park_id=3, activity_id=6))
db.session.add(ParkActivity(park_id=3, activity_id=5))
db.session.add(ParkActivity(park_id=3, activity_id=4))
db.session.add(ParkActivity(park_id=3, activity_id=3))
db.session.add(ParkActivity(park_id=4, activity_id=2))
db.session.add(ParkActivity(park_id=4, activity_id=9))
db.session.add(ParkActivity(park_id=4, activity_id=8))
db.session.add(ParkActivity(park_id=4, activity_id=7))
db.session.add(ParkActivity(park_id=4, activity_id=6))
db.session.add(ParkActivity(park_id=4, activity_id=5))
db.session.add(ParkActivity(park_id=4, activity_id=4))
db.session.add(ParkActivity(park_id=5, activity_id=2))
db.session.add(ParkActivity(park_id=5, activity_id=4))
db.session.add(ParkActivity(park_id=5, activity_id=6))
db.session.add(ParkActivity(park_id=5, activity_id=8))

db.session.add(Resource(resource_name="Basketball Court"))
db.session.add(Resource(resource_name="Bocce Ball Court"))
db.session.add(Resource(resource_name="Pool"))

db.session.add(Program(program_name="Youth Baseball (7-13)"))
db.session.add(Program(program_name="COED Softball"))
db.session.add(Program(program_name="Adult Swim Classes"))
db.session.add(Program(program_name="Water Polo"))
db.session.commit()

# start the flask loop
app.run()
