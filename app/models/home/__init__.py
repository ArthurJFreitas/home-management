from services.data-base-config import db

class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    residents = db.Column(db.String(120), unique=False, nullable=False)
    leader_id =  db.Column(db.String(120), unique=False, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username