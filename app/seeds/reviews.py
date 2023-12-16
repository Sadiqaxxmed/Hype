from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text

def seed_reviews():
    outfit1 = Review(
        review='This is a sick outfit!',
        rating=5,
        owner_id=2,
        outfit_id=1
    )
    outfit2 = Review(
        review='I love the colors!',
        rating=3,
        owner_id=1,
        outfit_id=2
    )
    outfit3 = Review(
        review='fire!!!!!!!!!',
        rating=5,
        owner_id=3,
        outfit_id=3
    )
    outfit4 = Review(
        review='nahhh this is not it',
        rating=2,
        owner_id=2,
        outfit_id=4
    )
    outfit5 = Review(
        review='yooo they got that ish on!!',
        rating=5,
        owner_id=3,
        outfit_id=5
    )
    outfit6 = Review(
        review='I love the colors!',
        rating=3,
        owner_id=1,
        outfit_id=6
    )
    outfit7 = Review(
        review='fire!!!!!!!!!',
        rating=5,
        owner_id=3,
        outfit_id=7
    )
    outfit8 = Review(
        review='nahhh this is not it',
        rating=2,
        owner_id=1,
        outfit_id=8
    )



    db.session.add(outfit1)
    db.session.add(outfit2)
    db.session.add(outfit3)
    db.session.add(outfit4)
    db.session.add(outfit5)
    db.session.add(outfit6)
    db.session.add(outfit7)
    db.session.add(outfit8)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))
        
    db.session.commit()


