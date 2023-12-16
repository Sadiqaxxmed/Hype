from flask import Blueprint, request
from app.models import User, Review, db
from flask_login import current_user, login_required

review_routes = Blueprint('review', __name__)


# Import and define your Review model here

# READ: Get a list of all reviews
@review_routes.route('/allReviews')
def get_reviews():

    reviews = Review.query.all()

    return {'reviews': [review.to_dict() for review in reviews]}

# READ: Get details of a specific review by ID
@review_routes.route('/allReviews/<int:id>')
def get_review(id):

    review = Review.query.get(id)

    if review:
        return {'reviews': review.to_dict()}
    return {'error': 'review not found'}, 404

# CREATE: Add a new review
@review_routes.route('/createReview', methods=['POST'])
def create_new_review():

        data = request.json

        new_review = Review(
            review=data['review'],
            rating=data['rating'],
            owner_id=data['owner_id'],
            outfit_id=data['outfit_id']
        )

        db.session.add(new_review)
        db.session.commit()
        
        return {'review': new_review.to_dict()}



# UPDATE: Update details of a specific review by ID
@review_routes.route('/updateReviews/<int:id>', methods=['PUT'])
def update_review(id):
        
        review = Review.query.get(id)

        if review:
            data = request.json
            review.review = data.get('review', review.review)
            review.rating = data.get('rating', review.rating)
            review.owner_id = data.get('owner_id', review.owner_id)
            review.outfit_id = data.get('outfit_id', review.outfit_id)

            db.session.commit()

            return {'review': review.to_dict()}


# DELETE: Delete a specific review by ID
@review_routes.route('/deleteReviews/<int:id>', methods=['DELETE'])
def delete_review(id):

    review = Review.query.get(id)

    if review:
        db.session.delete(review)
        db.session.commit()
        return {'message': 'Review deleted successfully'}


