from flask import Blueprint, request
from app.models import User, Outfit_Piece, db, Outfit
from flask_login import current_user, login_required

pieces_routes = Blueprint('pieces', __name__)

# Get all pieces by outfit id
@pieces_routes.route('/outfitDetails/<int:outfit_id>')
@login_required
def get_pieces(outfit_id):
    pieces = Outfit_Piece.query.filter(Outfit_Piece.outfit_id == outfit_id).all()
    return {'pieces': [piece.to_dict() for piece in pieces]}

# Add a piece to an outfit
@pieces_routes.route('/<int:id>', methods=['POST'])
@login_required
def add_piece(id):
    if current_user.id != Outfit.query.get(id).user_id:
        return {'errors': ['Unauthorized']}, 401
    piece = Outfit_Piece(
        outfit_id=id,
        piece_name=request.json['piece_name'],
        image=request.json['piece_image'],
        link=request.json['piece_link'],
        piece_price=request.json['piece_price'],
    )

    db.session.add(piece)
    db.session.commit()
    return piece.to_dict()

# Delete a piece from an outfit
@pieces_routes.route('/<int:id>', methods=['DELETE'])
# @login_required
def delete_piece(id):
    # if current_user.id != Outfit.query.get(id).user_id:
    #     return {'errors': ['Unauthorized']}, 401
    piece = Outfit_Piece.query.get(id)
    if piece.id:
        db.session.delete(piece)
        db.session.commit()

    return {'Piece Successfully Deleted': id}
