from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Ensure instance folder exists
    instance_path = os.path.join(app.root_path, '..', 'instance')
    if not os.path.exists(instance_path):
        os.makedirs(instance_path)
        print(f"Created instance directory at {instance_path}")

    # Set the database URI
    database_path = os.path.join(instance_path, 'reeds.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app import models  # Ensure models are imported

    with app.app_context():
        db.create_all()
        print(f"Database created at {database_path}")

    from app.routes import main
    app.register_blueprint(main)

    return app
