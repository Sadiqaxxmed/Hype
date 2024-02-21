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
@pieces_routes.route('/uploadOutfit/<int:outfit_id>', methods=['POST'])
@login_required
def add_pieces(outfit_id):
    print('OUTFIT ID!!!!!!!!!!!!!!!! ', outfit_id)
    if current_user.id != Outfit.query.get(outfit_id).owner_id:
        return {'errors': ['Unauthorized']}, 401

    pieces_data = request.get_json().get('pieces', [])

    added_pieces = []
    for piece_data in pieces_data:
        piece = Outfit_Piece(
            outfit_id=outfit_id,
            piece_name=piece_data['piece_name'],
            image=piece_data['piece_image'],
            link=piece_data['piece_link'],
            piece_price=piece_data['piece_price'],
        )
        db.session.add(piece)
        added_pieces.append(piece.to_dict())

    db.session.commit()
    return {'added_pieces': added_pieces}

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
