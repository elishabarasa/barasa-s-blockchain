
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from app.config import Config  # Make sure this import is correct


# # Initialize the database object
# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)

#   # Use Config class directly
#     app.config.from_object(Config)
#    # Print the config for debugging purposes
#     print(f"Config Loaded: {app.config}")


#     # Initialize the database with app
#     db.init_app(app)
    
#     # Register blueprints
#     from .blueprints.main import main
#     from .blueprints.donations import donations_bp
#     from .blueprints.auth import auth_bp
#     from .blueprints.products import products_bp
    
#     app.register_blueprint(main)
#     app.register_blueprint(donations_bp, url_prefix='/donations')
#     app.register_blueprint(auth_bp, url_prefix='/auth')
#     app.register_blueprint(products_bp, url_prefix='/products')

#     return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Flask-Migrate for handling migrations
from app.config import Config  # Ensure this import is correct

# Initialize the database and migration objects
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Use Config class directly
    app.config.from_object(Config)

    # Print the config for debugging purposes (remove this in production)
    print(f"Config Loaded: {app.config}")

    # Initialize the database and migration with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .blueprints.main import main
    from .blueprints.donations import donations_bp
    from .blueprints.auth import auth_bp
    from .blueprints.products import products_bp

    app.register_blueprint(main)
    app.register_blueprint(donations_bp, url_prefix='/donations')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(products_bp, url_prefix='/products')

    return app
