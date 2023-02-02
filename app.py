from flask import Flask,request,jsonify   #jsonify func assigns para dynamically and that para becomes key of the dict
from uuid import uuid1,uuid4
import json,pytz
from datetime import date, datetime
import pandas as pd
import numpy as np
from flask_cors import CORS
from config import db, SECRET_KEY
from os import environ, path, getcwd
from dotenv import load_dotenv
from models.user import User
from models.discover import Discover
# from models.yoursubscriptions import Your_Subscriptions
from models.ott import OTT
from models.news import News
from models.health import Health
from models.music import Music
from models.payment import Payment
from models.paymentdetails import Payment_Details

load_dotenv(path.join(getcwd(),'.env'))
def create_app():
    app=Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI']=environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False
    app.config['SQLALCHEMY_ECHO']=False
    app.secret_key=SECRET_KEY
    
    db.init_app(app)
    print("DB intialized successfully")
    with app.app_context():
        @app.route('/signup', methods=['POST'])
        def signup():
            data=request.form.to_dict(flat=True)
            new_user=User(
                name=data['name'],
                email=data['email'],
                password=data['password'],
                username=data['username'],
                phoneno=data['phoneno'],
                paymentmode=data['paymentmode'],
                paymentdetails=data['paymentdetails']
            )
            db.session.add(new_user)
            db.session.commit()
            return jsonify(msg="User Added Successfully")
        
        @app.route('/login',methods=['POST'])
        def login():
            email=request.args.get('email')  
            password=request.args.get('password')  
            # for element in db:
            user=(User.query.filter_by(email=email).first() and User.query.filter_by(password=password).first())
            # for element in user:               
            #     if element["email"]==email and  element["password"]==password :
            #         useridx=suser.index(elements)
            #         response={
            #             "message":"Login Successful",
            #             "user_index":useridx
            #         }
            #         return response
            #     else:
            #         continue
            # return "Incorrect email id or password.Please Try Again!"
            data=request.get_json()
            useridx=User(
                user.id
            )
            return useridx and jsonify(msg="login successful" )
        
        @app.route('/add_paymentmode', methods=['POST'])
        def add_paymentmode():
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
        
        @app.route('/add_paymentdetails', methods=['POST'])
        def add_paymentdetails():
            data=request.get_json()
            username=request.args.get('username')
            user=User.query.filter_by(username=username).first()
            user_details=Payment_Details(
                payment_details1=data['upi id/card no/crn'],
                payment_details2=data['mpin/validity/mpin'],
                payment_details3=data['cvv'],
                user_id=user.id
            )
            db.session.add(user_details)
            db.session.commit()
            return jsonify(msg="payment details stored successfully...")
        
        @app.route('/logout',methods=['POST'])
        def logout():
            username=request.args.get('username')
            user=User.query.filter_by(username=username).first()
            db.session.exit(user)
            db.session.commit()
            return jsonify(msg="you have logged out successfully")
           
        # @app.route('/my_subscriptions', methods=['GET'])
        # def my_subscriptions():
        #     username=request.args.get('username')
        #     user=User.query.filter_by(username=username).first()
        #     your_subscriptions=Your_Subscriptions.query.filter_by(user_id=user.id).first()
        #     Your_Subscriptions_data={
        #         "products": your_subscriptions.products_purchased,
        #         "purchase_type":your_subscriptions.service_type,
        #         "renewal_date":your_subscriptions.renewal_date,
        #         "renewal_amount":your_subscriptions.renewal_amount,
        #         "renewal_time":your_subscriptions.renewal_time
        #     }
        #     return Your_Subscriptions_data
        
        @app.route('/discover_products',methods=['GET'])
        def discover_products():
            
            products={}
            for element in discover:
                discover_data.append({
                    "category": element.categories
                })
                products["categories"]=discover_data
            return products 
        # if cmd == "ott":
        #     choosen_route=(app.route('/discover_ott',methods=['GET']))
        # if cmd == "music":
        #     choosen_route=(app.route('/discover_music',methods=['GET']))
        # if cmd == "news":
        #     choosen_route=(app.route('/discover_news',methods=['GET']))
        # if cmd == "health":
        #     choosen_route=(app.route('/discover_health',methods=['GET']))
        @app.route('/discover_ott',methods=['GET'])
        def discover_ott():
            
            products={}
            for element in ott:
                discover_data.append({
                    "platforms": element.platform_name
                })
                products["platforms"]=discover_data
            return products 
        @app.route('/discover_music',methods=['GET'])
        def discover_music():
            
            products={}
            for element in music:
                discover_data.append({
                    "platforms": element.platform_name
                })
                products["platforms"]=discover_data
            return products 
        @app.route('/discover_news',methods=['GET'])
        def discover_news():
            
            products={}
            for element in news:
                discover_data.append({
                    "platforms": element.platform_name
                })
                products["platforms"]=discover_data
            return products     
        @app.route('/discover_health',methods=['GET'])
        def discover_health():
            
            products={}
            for element in health:
                discover_data.append({
                    "platforms": element.platform_name
                })
                products["platforms"]=discover_data
            return products 
        
        @app.route('/add_categories',methods=['POST'])
        def add_categories():
            recv_username=request.args.get('username')
            category_data=request.get_json()
            if recv_username=="admin":
                for data in category_data["data"]:
                    new_category=Discover(
                        categories=data['category'],
                        categories_key=data['category key']
                    )
                db.session.add(new_category)
                db.session.commit()
            return jsonify(msg="category added")
        @app.route('/add_ott',methods=['POST'])
        def add_ott():
            recv_username=request.args.get('username')
            ott_data=request.get_json()
            if recv_username=="admin":
                for data in ott_data["data"]:
                    new_platform=OTT(
                        platform_name=data['category'],
                        platform_key=data['category key']
                    )
                db.session.add(new_platform)
                db.session.commit()
            return jsonify(msg="ott added")
        @app.route('/add_music',methods=['POST'])
        def add_music():
            recv_username=request.args.get('username')
            music_data=request.get_json()
            if recv_username=="admin":
                for data in music_data["data"]:
                    new_platform=Music()(
                        platform_name=data['category'],
                        platform_key=data['category key']
                    )
                db.session.add(new_platform)
                db.session.commit()
            return jsonify(msg="music added")
        @app.route('/add_news',methods=['POST'])
        def add_news():
            recv_username=request.args.get('username')
            news_data=request.get_json()
            if recv_username=="admin":
                for data in news_data["data"]:
                    new_platform=News(
                        platform_name=data['category'],
                        platform_key=data['category key']
                    )
                db.session.add(new_platform)
                db.session.commit()
            return jsonify(msg="news added")
        
        @app.route('/add_health',methods=['POST'])
        def add_health():
            recv_username=request.args.get('username')
            health_data=request.get_json()
            if recv_username=="admin":
                for data in health_data["data"]:
                    new_platform=Health()(
                        platform_name=data['category'],
                        platform_key=data['category key']
                    )
                db.session.add(new_platform)
                db.session.commit()
            return jsonify(msg="health added")
            
               
            
            
        # db.drop_all()
        db.create_all()
        db.session.commit()
        return app


if __name__=='__main__':
    app= create_app()
    app.run(debug=True)