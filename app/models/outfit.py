from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import ForeignKey



class Outfit(db.Model):
    __tablename__ = 'outfits'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, ForeignKey(add_prefix_for_prod('users.id')))
    description = db.Column(db.String, nullable=False)
    outfitPrice = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(), nullable=False)
    catagory = db.Column(db.String(), nullable=False)

    user = db.relationship('User', back_populates='outfits')
    outfit_pieces = db.relationship('Outfit_Piece', back_populates='outfit')
    reviews = db.relationship('Review', back_populates='outfit')

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'outfitPrice': self.outfitPrice,
            'image': self.image,
            'catagory': self.catagory,
            'owner_id': self.owner_id
        }
