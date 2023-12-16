from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import ForeignKey


class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer(), primary_key=True)
    review = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Integer(), nullable=False)
    owner_id = db.Column(db.Integer, ForeignKey (add_prefix_for_prod('users.id')))
    outfit_id = db.Column(db.Integer, ForeignKey (add_prefix_for_prod('outfits.id')))

    user = db.relationship('User', back_populates='reviews')
    outfit = db.relationship('Outfit', back_populates='reviews')

    def to_dict(self):
        return {
            'id': self.id,
            'review': self.review,
            'rating': self.rating,
            'owner_id': self.owner_id,
            'outfit_id': self.outfit_id
        }