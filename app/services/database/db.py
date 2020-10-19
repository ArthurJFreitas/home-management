from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from app import app

DB_URL = 'postgresql+psycopg2://postgres:postgres123@localhost:5432/home-management'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning



db.create_all()