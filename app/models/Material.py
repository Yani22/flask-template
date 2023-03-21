from app import db
from utils.date import current_datetime


class Material(db.Model):
    __tablename__ = 'Material'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    project_id = db.Column(db.Integer, db.ForeignKey('Project.id'), nullable=False)
    material_name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.Date, nullable=False, default=current_datetime())
    date_updated = db.Column(db.Date, nullable=False, default=current_datetime())