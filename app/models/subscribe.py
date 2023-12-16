from .db import db, add_prefix_for_prod, environment, SCHEMA
from datetime import datetime

subscriptions = db.Table(
    'subscriptions',
    db.Model.metadata,
    db.Column('subscriber_id', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), primary_key=True),
    db.Column('subscribed_id', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), primary_key=True),
    db.Column('created_at', db.DateTime, default=datetime.utcnow)
)

if environment == 'production':
    subscriptions.schema = SCHEMA