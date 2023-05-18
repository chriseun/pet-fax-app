from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

#config routes
    @app.route('/')
    def hello():
      return 'Hello, PetFax!'

  # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    # from . import fact
    # app.register_blueprint(fact.bp)

  #return app
    return app

# factory
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/petfax'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


from . import models
models.db.init_app(app)
migrate = Migrate(app, models.db)

# from flask import Flask

# def create_app():
#     app = Flask(__name__)

#     @app.route('/')
#     def hello():
#         return 'Hello, PetFax!'

#     return app
