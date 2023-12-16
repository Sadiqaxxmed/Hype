from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import ForeignKey


class Outfit_Piece(db.Model):
    __tablename__ = "outfit_pieces"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    outfit_id = db.Column(db.Integer, ForeignKey(add_prefix_for_prod('outfits.id')))
    piece_name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)
    piece_price = db.Column(db.Float, nullable=False)

    outfit = db.relationship('Outfit', back_populates='outfit_pieces')

    def to_dict(self):
        return {
            'id': self.id,
            'piece_name': self.piece_name,
            'image': self.image,
            'link': self.link,
            'piece_price': self.piece_price,
            'outfit_id': self.outfit_id
        }