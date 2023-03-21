from app import db
from utils.date import current_datetime


class ProjectDetails(db.Model):
    __tablename__ = 'ProjectDetails'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    project_id = db.Column(db.Integer, db.ForeignKey('Project.id'), nullable=False)
    engineer = db.Column(db.String(200), nullable=False)
    architect = db.Column(db.String(250), nullable=False)
    project_manager = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.Date, nullable=False, default=current_datetime())
    date_updated = db.Column(db.Date, nullable=False, default=current_datetime())