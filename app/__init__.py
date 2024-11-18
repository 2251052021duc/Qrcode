from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote



app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/data_personal?charset=utf8mb4" % quote("123456789a")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8


db = SQLAlchemy(app)
data_personal = db

