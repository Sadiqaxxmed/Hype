from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import User, db

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()
@user_routes.route('/<int:id>', methods=['PUT'])
@login_required
def edit_user(id):
    user = User.query.get(id)
    user.username = request.json['username']
    user.email = request.json['email']
    user.profile_image = request.json['profile_image']
    user.bio = request.json['bio']
    user.password = request.json['password']

    db.session.commit()
    return user.to_dict()
   

@user_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_user(id):
    user = User.query.get(id)
    if user.id:
        db.session.delete(user)
        db.session.commit()

    return {'User Successfully Deleted': id}


    #subscribed to
@user_routes.route('/<int:id>/subscribed')
# @login_required
def subscribed(id):
    user = User.query.get(id)
    return {'subscribed': [subscribed.to_dict() for subscribed in user.subscribed]}


    #subscribers
@user_routes.route('/<int:id>/subscribers')
# @login_required
def subscribers(id):
    user = User.query.get(id)
    return {'subscribers': [subscriber.to_dict() for subscriber in user.subscribers]}

    #subscribe to a user
@user_routes.route('/<int:id>/subscribe', methods=['POST'])
@login_required
def subscribe(id):
    user = User.query.get(id)
    user.subscribers.append(current_user)
    db.session.commit()
    return user.to_dict()

    #unsubscribe from a user
@user_routes.route('/<int:id>/unsubscribe', methods=['POST'])
@login_required
def unsubscribe(id):
    user = User.query.get(id)
    user.subscribers.remove(current_user)
    db.session.commit()
    return user.to_dict()


    