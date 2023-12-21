from flask import Blueprint, request
from app.models import User, Outfit, db
from flask_login import current_user, login_required

outfit_routes = Blueprint('outfit', __name__)


# READ: Get a list of all outfits
@outfit_routes.route('/allOutfits')
def get_outfits():

    outfits = Outfit.query.all()

    return {'outfits': [outfit.to_dict() for outfit in outfits]}


# READ: Get details of a specific outfit by ID
@outfit_routes.route('/allOutfits/<int:id>')
def get_outfit(id):

    outfit = Outfit.query.get(id)

    if outfit:
        return {'outfits': outfit.to_dict()}
    
    return {'error': 'Outfit not found'}, 404


# CREATE: Add a new outfit
@outfit_routes.route('/uploadOutfit/<int:user_id>', methods=['POST'])
@login_required
def create_new_outfit(user_id):

    data = request.form
    
    outfit = Outfit(
            owner_id=data['owner_id'],
            description=data['description'],
            outfitPrice=data['outfitPrice'],
            image=data['image'],
            catagory=data['catagory']
    )
    
    db.session.add(outfit)
    db.session.commit()

    return {'outfit': outfit.to_dict()}


# UPDATE: Update details of a specific outfit by ID
@outfit_routes.route('/updateOutfits/<int:outfit_id>', methods=['PUT'])
@login_required
def update_outfit(outfit_id):
        
        outfit = Outfit.query.get(outfit_id)

        if outfit:
            data = request.form
            # outfit.owner_id = data.get('owner_id', outfit.owner_id)
            outfit.description = data["description"]
            outfit.outfitPrice = data["outfitPrice"]
            outfit.image = data["image"]
            outfit.catagory = data["catagory"]

            db.session.commit()

            return {'outfit': outfit.to_dict()}

        
        return {'error': 'Outfit not found'}, 404


# DELETE: Delete a specific outfit by ID
@outfit_routes.route('/deleteOutfits/<int:outfit_id>', methods=['DELETE'])
@login_required
def delete_outfit(outfit_id):

    outfit = Outfit.query.get(outfit_id)

    if outfit:
        db.session.delete(outfit)
        db.session.commit()
        return {'message': 'Outfit deleted successfully'}
    
    return {'error': 'Outfit not found'}, 404
