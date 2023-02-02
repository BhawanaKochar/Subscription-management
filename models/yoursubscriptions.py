from config import db
class Your_Subscriptions():
    __tablename__='your_subscriptions'
    id=db.Column(db.Integer,primary_key=True)
    product_purchased=db.Column(db.String(200),unique=True)
    category_key=db.Column(db.String(200),db.ForeignKey('discover.category_key'))
    user_id=db.Column(db.String(200),db.ForeignKey('user.id'))
    product_purchase_type=db.Column(db.String(200),nullable=False)
    service_type=db.Column(db.String(200),nullable=False)
    renewal_date=db.Column(db.DateTime,nullable=False)
    renewal_time=db.Column(db.DateTime,nullable=False)
    renewal_amount=db.Column(db.String(200),nullable=False)
    