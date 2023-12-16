from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
import random


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Lil Boat', profile_image='data:image/jpeg;base64,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', bio='Please dont copy my style 👁️', email='demo@aa.io', password='password')
    brentfaiyaz = User(
        username='Brent Faiyaz', profile_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmVmO9Vlg3H3wGWRiBnWUtLZjjXAI_7vOFng&usqp=CAU', bio='Here share a bit of what I call fashion.',  email='Brent@aa.io', password='password')
    sza = User(
        username='SZA', profile_image='data:image/jpeg;base64,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', bio='...---...',  email='SZA@aa.io', password='password')

    db.session.add(demo)
    db.session.add(brentfaiyaz)
    db.session.add(sza)
    db.session.commit()


    def add_subscription_relationships(subscriber, users_to_subscribe):
        for user_to_subscribe in users_to_subscribe:
            subscriber.subscribe(user_to_subscribe)

    all_users = [demo, brentfaiyaz, sza]  # Add the rest of your user objects to this list

    for user in all_users:
        other_users = [u for u in all_users if u != user]
        users_to_subscribe = random.sample(other_users, 2)  # Adjust the number as needed
        add_subscription_relationships(user, users_to_subscribe)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()