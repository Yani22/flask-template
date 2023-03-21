from app import db
from utils.date import current_datetime


class Project(db.Model):
    __tablename__ = 'Project'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    date_updated = db.Column(db.Date, nullable=False, default=current_datetime())
    date_created = db.Column(db.Date, nullable=False, default=current_datetime())