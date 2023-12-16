from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from .subscribe import subscriptions
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    profile_image = db.Column(db.String, nullable=False)
    bio = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    outfits = db.relationship('Outfit', back_populates='user')
    reviews = db.relationship('Review', back_populates='user')

    subscribed = db.relationship('User', secondary=subscriptions,
                                primaryjoin=(subscriptions.c.subscriber_id == id),
                                secondaryjoin=(subscriptions.c.subscribed_id == id),
                                backref=db.backref('subscribers', lazy='dynamic'), lazy='dynamic')


    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    
    def subscribe(self, user):
        if not self.is_subscribed(user):
            self.subscribed.append(user)
            return self
        
    def unsubscribe(self, user):
        if self.is_subscribed(user):
            self.subscribed.remove(user)
            return self
    
    def is_subscribed(self, user):
        return self.subscribed.filter(subscriptions.c.subscribed_id == user.id).count() > 0
    
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'profile_image': self.profile_image,
            'bio': self.bio,
            'email': self.email
        }
    
    def to_dict_with_subscribers(self):
        return {
            'id': self.id,
            'username': self.username,
            'profile_image': self.profile_image,
            'bio': self.bio,
            'subscribers': [subscriber.to_dict() for subscriber in self.subscribers]
        }
