"""Seed database with sample data from CSV Files."""

from models import db
from app import app


db.drop_all()
db.create_all()



db.session.commit()
