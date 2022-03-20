"""Seed database with sample data from CSV Files."""

from csv import DictReader
from app import db
from models import User


db.create_all()



db.session.commit()
