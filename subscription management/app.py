from flask import Flask, jsonify, request
from flask_cors import CORS
from config import db, SECRET_KEY
from os import environ, path, getcwd
from dotenv import load_dotenv
from model.payment import Payment

load_dotenv(path.join(getcwd(), '.env'))

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = False
    app.secret_key = SECRET_KEY
    db.init_app(app)
    print("DB Initialized Sucessfully")

    CORS(app)

    with app.app_context():
        @app.route('/payment', methods=['POST'])
        def payment():
            data=request.get_json()
            username=request.args.get('username')
            user=User.query.filter_by(username=username).first()
            user_details=Payment(
                UPI=data['upi'],
                credits=data['credits'],
                debits=data['debits'],
                netbanking=data['netbanking'],
                user_id=user.id
            )
            db.session.add(user_details)
            db.session.commit()
            return jsonify(msg="payment details stored successfully...")
            
            
