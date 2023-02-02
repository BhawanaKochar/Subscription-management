from config import db
class Payment_Details(db.Model):
     _tablename_ = 'payment_details'
     id=db.Column(db.Integer, primary_key=True)
     user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
     payment_details1=db.Column(db.String(200), unique=True,nullable=False)
     payment_details2=db.Column(db.String(200), unique=True,nullable=True)
     payment_details3=db.Column(db.String(200), unique=True,nullable=True)
     