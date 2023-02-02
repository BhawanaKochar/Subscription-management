from config import db
class OTT():
    __tablename__='ott'
    id=db.Column(db.Integer,primary_key=True)
    platform_name=db.Column(db.String(200),unique=True,nullable=False)
    platform_key=db.Column(db.String(200),unique=True,nullable=False)
    category_key=db.Column(db.String(200),db.ForeignKey('discover.category_key'))