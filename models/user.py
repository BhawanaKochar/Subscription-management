from config import db
class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(200),unique=True,nullable=False)
    name=db.Column(db.String(200),unique=False,nullable=False)
    phoneno=db.Column(db.String(200),unique=True,nullable=False)
    email=db.Column(db.String(200),unique=True,nullable=False)
    password=db.Column(db.String(200),nullable=False,unique=False)
    paymentdetails=db.Column(db.String(200),nullable=False,unique=True)
    paymentmode=db.Column(db.String(200),unique=False,nullable=False)
    payment=db.relationship('Payment',backref='user')
    payment_details=db.relationship('Payment_Details',backref='user')
    # your_subscriptions=db.relationship('Your_Subscriptions',backref='user')
    