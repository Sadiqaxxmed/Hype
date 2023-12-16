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
@outfit_routes.route('/newOutfit', methods=['POST'])
def create_new_outfit():

    data = request.json
    
    new_outfit = Outfit(
            owner_id=data['owner_id'],
            description=data['description'],
            outfitPrice=data['outfitPrice'],
            image=data['image'],
            catagory=data['catagory']
    )

    db.session.add(new_outfit)
    db.session.commit()

    return {'outfit': new_outfit.to_dict()}


# UPDATE: Update details of a specific outfit by ID
@outfit_routes.route('/updateOutfits/<int:id>', methods=['PUT'])
def update_outfit(id):
        
        outfit = Outfit.query.get(id)

        if outfit:
            data = request.json
            outfit.owner_id = data.get('owner_id', outfit.owner_id)
            outfit.description = data.get('description', outfit.description)
            outfit.outfitPrice = data.get('outfitPrice', outfit.outfitPrice)
            outfit.image = data.get('image', outfit.image)
            outfit.catagory = data.get('catagory', outfit.catagory)

            db.session.commit()

            return {'outfit': outfit.to_dict()}

        
        return {'error': 'Outfit not found'}, 404


# DELETE: Delete a specific outfit by ID
@outfit_routes.route('/deleteOufits/<int:id>', methods=['DELETE'])
def delete_outfit(id):

    outfit = Outfit.query.get(id)

    if outfit:
        db.session.delete(outfit)
        db.session.commit()
        return {'message': 'Outfit deleted successfully'}
    
    return {'error': 'Outfit not found'}, 404
