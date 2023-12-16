from app.models import db, Outfit, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_outfits():
    outfit1 = Outfit(
        description='This outfit beggs for attention',
        outfitPrice=12037,
        catagory='streetwear',
        image='https://tinyurl.com/5hcszuf6',
        owner_id=1
    )
    outfit2 = Outfit(
        description='Really cute for a date night out.',
        outfitPrice=958,
        catagory='date night',
        image='https://tinyurl.com/2stha4jk',
        owner_id=3
    )
    outfit3 = Outfit(
        description='I mean what more do I have to say.',
        outfitPrice=1124,
        catagory='casual',
        image='https://tinyurl.com/4b76c663',
        owner_id=2
    )
    outfit4 = Outfit(
        description='Theres a lot going on here but it works 😅',
        outfitPrice=2358,
        catagory='streetwear',
        image='https://assets.vogue.com/photos/58d1b1033a42674dbedc29d6/master/w_1600%2Cc_limit/04-sza.jpg',
        owner_id=3
    )
    outfit5 = Outfit(
        description='U trYna look cooll dawg?',
        outfitPrice=1556,
        catagory='streetwear',
        image='https://assets.vogue.com/photos/58912f1297a3db337a248b47/master/w_1600%2Cc_limit/02-lilyachty.jpg',
        owner_id=1
    )
    outfit6 = Outfit(
        description='Real laid back fit. Nice if you are in a rush and you are trying to throw something on.',
        outfitPrice=543,
        catagory='streetwear',
        image='https://tinyurl.com/hy6jcmek',
        owner_id=3
    )
    outfit7 = Outfit(
        description='Theres a reason Im smiling!',
        outfitPrice=841,
        catagory='streetwear',
        image='https://www.highsnobiety.com/static-assets/dato/1682691832-lil-yachty-outfits-style-04.jpg',
        owner_id=1
    )
    outfit8 = Outfit(
        description='This fit has you feeling like a million bucks',
        outfitPrice=648,
        catagory='streetwear',
        image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQM8hD39eTesJ1BqQz4os2xmoguMbHm2JxYYw&usqp=CAU',
        owner_id=2
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


# Uses a raw SQL query to TRUNCATE or DELETE the songs table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_outfits():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.outfits RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM outfits"))

    db.session.commit()