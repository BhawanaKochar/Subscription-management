from config import db
class Payment(db.Model):
     _tablename_ = 'payment'
     id=db.Column(db.Integer, primary_key=True)
     UPI=db.Column(db.String(200), primary_key=True)
     credits=db.Column(db.String(200), nullable=False)
     debits=db.Column(db.String(200), nullable=False)
     netbanking=db.Column(db.String(200), nullable=False)
     user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)