from config import db
class Discover():
    __tablename__='discover'
    id=db.Column(db.Integer,primary_key=True)
    categories=db.Column(db.String(200),unique=True,nullable=False)
    categories_key=db.Column(db.String(200),unique=True,nullable=False)
    ott=db.relationship('OTT',backref='discover')
    news=db.relationship('News',backref='discover')
    health=db.relationship('Health',backref='discover')
    music=db.relationship('Music',backref='discover')

"""#respositroy created settings collaborators manage access add team members"""