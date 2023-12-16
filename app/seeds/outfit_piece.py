from app.models import db, Outfit_Piece, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_outfit_pieces():
    piece1 = Outfit_Piece(
        piece_name='Ferrari Race Hooded', 
        image="https://images.puma.com/image/upload/f_auto,q_auto,b_rgb:fafafa,w_750,h_750/global/533745/02/mod01/fnd/PNA/fmt/png/Scuderia-Ferrari-Race-Hooded-Men's-Sweat-Jacket", 
        link='Cj0KCQjwmvSoBhDOARIsAK6aV7h0RpDdr4gDf0fqGBthHxTbuGtp9vi6tskOOnFyKLxi8VxejuNA288aAlCOEALw_wcB', 
        piece_price= 60.00,
        outfit_id=1
    )
    piece2 = Outfit_Piece(
        piece_name='D271 STAR STRAIGHT DENIM', 
        image='https://mnml.la/cdn/shop/products/D271-Star-Straight-Denim-Blue-2_540x.jpg?v=1659177521', 
        link='https://mnml.la/products/mnml-denim-d271-star-denim-m2020-d996-blu?variant=35442801115208&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&utm_source=google&utm_medium=paid&utm_campaign=20249513409&utm_content=&utm_term=&gadid=&gclid=Cj0KCQjwmvSoBhDOARIsAK6aV7iHcGshtLfBerz-9fCpdd2_TfjVNQajEFg5OurUVL0omSx81hwgibIaAlavEALw_wcB', 
        piece_price= 48.00,
        outfit_id=1
    )
    piece3 = Outfit_Piece(
        piece_name='Nike Air Force 1 07', 
        image='https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/b7d9211c-26e7-431a-ac24-b0540fb3c00f/air-force-1-07-mens-shoes-jBrhbr.png', 
        link='https://www.nike.com/t/air-force-1-07-mens-shoes-jBrhbr/CW2288-111?nikemt=true&cp=68540849105_search_--x-20301353919---c-----9033291-13071857-00194500874985&gclid=Cj0KCQjwmvSoBhDOARIsAK6aV7g76TiMuZy2I9Jzi6eBusjRGCRvbQeUOuF1EmuG6fyM_H-P5JFBzwkaAgGqEALw_wcB&gclsrc=aw.ds', 
        piece_price= 110.00,
        outfit_id=1
    )
    piece4 = Outfit_Piece(
        piece_name='SATINIOR Trawler Beanie', 
        image='https://m.media-amazon.com/images/I/81fZN-ke52S._AC_UX385_.jpg', 
        link='Cj0KCQjwmvSoBhDOARIsAK6aV7jmkSWAYrcHAr9Et_sroWWbcV5i9wQvqyhT2Bk6mT84zWbspqxHpkAaApiuEALw_wcB', 
        piece_price= 6.99,
        outfit_id=1
    )
    piece5 = Outfit_Piece(
        piece_name='Halter Backless Slit Maxi Dress', 
        image='https://saledress.com/cdn/shop/products/14_1fa2b253-7e45-4cc2-af8c-fa8bc7d77e02.jpg?v=1663134570&width=600', 
        link='https://saledress.com/products/myf-k10124?variant=41782523166902&epik=dj0yJnU9UHFSTXdLWVN4ZVpxalpXZ2c0NndzT3g0VHIzMkRtVE0mcD0wJm49NHl6azEwZE5sZ0FjZXJnRXpqUExZQSZ0PUFBQUFBR1VneVpj', 
        piece_price= 150.99,
        outfit_id=2
    )
    piece6 = Outfit_Piece(
        piece_name='Givenchy Shark Print T-shirt', 
        image='https://www.fashionnova.com/cdn/shop/products/08-21-20Studio4_CE_SD_10-16-11_20_SUGARCOATED_Nude_4718_JK_468x.jpg?v=1598293309', 
        link='https://www.fashionnova.com/products/tied-together-embellished-heels-nude?variant=12201738862716&utm_source=google&utm_medium=cpc&utm_id=20463356330&utm_campaign=gg_nb_performance_max_smart_womens_shoes&gclid=CjwKCAjw4P6oBhBsEiwAKYVkq3XIZwwrRw6ZnCiNAU_xbrsXzUnI7gMtvfZ58mfyMFhOWv_1ynqmpxoCaWQQAvD_BwE', 
        piece_price= 80.99,
        outfit_id=2
    )
    piece7 = Outfit_Piece(
        piece_name='Tommy Hilfiger Monogram Varsity V Neck', 
        image= 'https://www.davidjones.com/productimages/magnify/1/2499520_22103673_9081318.jpg',
        link= 'https://www.davidjones.com/product/tommy-hilfiger-monogram-varsity-v-neck-25664631',
        piece_price= 199.99,
        outfit_id=3
    )
    piece8 = Outfit_Piece(
        piece_name='Daniel Ellissa Mens Wide Leg Pants - Double Pleated', 
        image= 'https://tinyurl.com/ytmb36ux',
        link= 'https://tinyurl.com/4nf79yj8',
        piece_price= 60.00,
        outfit_id=3
    )
    piece9 = Outfit_Piece(  
        piece_name='The Ellis Penny Loafer', 
        image= 'https://tinyurl.com/58p42fue',
        link= 'https://tinyurl.com/5c2zafp6',
        piece_price= 375.00 ,
        outfit_id=3
    )
    piece10 = Outfit_Piece(
        piece_name='Sunglasses Round Prada', 
        image= 'https://tinyurl.com/23w6cj2h',
        link= 'https://tinyurl.com/2p9yczwv',
        piece_price= 870.00,
        outfit_id=3
    )
    piece11 = Outfit_Piece(
        piece_name='Real Tree Camo Jacket', 
        image= 'https://cdn11.bigcommerce.com/s-mplfu2e611/images/stencil/320w/products/95965/171188/Real-Tree-Camoflauge-Jacket-5__71346.1666808367.jpg?c=1',
        link= 'https://ragstock.com/shop/real-tree-camouflage-jacket',
        piece_price= 19.00,
        outfit_id=4
    )
    piece12 = Outfit_Piece(
        piece_name='Oversized Tan Hoodie',
        image= 'https://m.media-amazon.com/images/I/51PcruQZPiL._AC_UX569_.jpg',
        link= 'https://www.amazon.com/Lauweion-Sweatshirt-Kangaroo-Shoulder-Pullovers/dp/B09PH6L16P/ref=asc_df_B09PH6L16P/?tag=hyprod-20&linkCode=df0&hvadid=647200365765&hvpos=&hvnetw=g&hvrand=6132912186103003882&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9019630&hvtargid=pla-1895492867173&psc=1&gclid=CjwKCAjw4P6oBhBsEiwAKYVkqwZ707EN1QOcHuMCTGCCCEbxCqQ-z4MD6N5Ym4QzAu3bv71KOcVlMhoCDaUQAvD_BwE',
        piece_price=34.00,
        outfit_id=4
    )
    piece13 = Outfit_Piece(
        piece_name='Oversized Camo Joggers', 
        image= 'https://media.boohoo.com/i/boohoo/fzz01571_multi_xl_1/female-multi-oversized-camo-slogan-joggers?w=450&qlt=default&fmt.jp2.qlt=70&fmt=auto&sm=fit',
        link= 'https://www.fashionnova.com/products/no-regrets-camo-cargo-pant-olive-combo?variant=39262027186300&utm_source=google&utm_medium=cpc&utm_id=20463356384&utm_campaign=gg_nb_performance_max_smart_womens_curve&gclid=CjwKCAjw4P6oBhBsEiwAKYVkq5Mdrz6UgRcR96xCLFGGOPwSWQve9O8G9lA7B4NXnFFei4gmnLpA0xoCD-wQAvD_BwE',
        piece_price=80.00,
        outfit_id=4
    )
    piece14 = Outfit_Piece(
        piece_name='Adidas Gazelle Bold', 
        image= 'https://www.kickscrew.com/cdn/shop/products/main-square_68a9f573-347c-41d8-8373-3a107c1e625c_540x.jpg?v=1694120906',
        link= 'https://stockx.com/adidas-gazelle-bold-grey-white-w',
        piece_price= 110.00,
        outfit_id=4
    )
    piece15 = Outfit_Piece(
        piece_name='Red Skins Tan Varsity Jacket', 
        image='https://i.ebayimg.com/images/g/qowAAOSwd2VfOZDi/s-l1600.jpg', 
        link='https://www.ebay.com/itm/254690031789', 
        piece_price=195.00,
        outfit_id=5
    )
    piece16 = Outfit_Piece(
        piece_name='Ripped Straight Leg Jeans', 
        image='https://di2ponv0v5otw.cloudfront.net/posts/2023/04/25/644882a8678c3a652e730848/m_wp_644882be24237ae6170669db.webp', 
        link='https://poshmark.com/listing/Khaite-Kyle-Straight-Leg-Jeans-Size-26-644882a8678c3a652e730848', 
        piece_price= 325.00,
        outfit_id=5
    )
    piece17 = Outfit_Piece(
        piece_name='Air Jordan 1 Retro High OG Patent Bred', 
        image='https://image.goat.com/transform/v1/attachments/product_template_additional_pictures/images/062/992/408/original/784379_01.jpg.jpeg?action=crop&width=400', 
        link='https://www.goat.com/sneakers/air-jordan-1-retro-high-og-patent-bred-555088-063?utm_source=google_ads&utm_medium=cpc&utm_campaign=20272243100&utm_content=&gclid=CjwKCAjwvfmoBhAwEiwAG2tqzMAkT6x2ZVqhqmjyG6bkV37y0x9t5ZrRwWdqv_o-PnzPXH2bz-sGYxoCVtwQAvD_BwE', 
        piece_price=200.99,
        outfit_id=5
    )
    piece18 = Outfit_Piece(
        piece_name='Givenchy Shark Print T-shirt', 
        image='https://fuckingyoung.es/wp-content/uploads/2012/06/gyvenchi_sharp2.jpg', 
        link='https://fuckingyoung.es/givenchy-shark-print-t-shirt/', 
        piece_price=20.99,
        outfit_id=6
    )
    piece19 = Outfit_Piece(
        piece_name='Chelsea Drop Waist Baggy Jean', 
        image='https://www.fashionnova.com/cdn/shop/files/08-29-23Studio1_TH_11-56-12_17_fn24887ft46_MediumWash_R_20449_SG_468x.jpg?v=1693946946', 
        link='https://www.fashionnova.com/products/chelsea-drop-waist-baggy-jeans-medium-wash?variant=39267523002492&utm_source=google&utm_medium=cpc&utm_id=20463356342&utm_campaign=gg_nb_performance_max_smart_womens_jeans&gclid=CjwKCAjw4P6oBhBsEiwAKYVkqxTcoZ-6lwknQyUWPjBV_239qjSHKk6Lm-0kVQPzUydMFvH2E3G7TBoCvdAQAvD_BwE', 
        piece_price=55.00,
        outfit_id=6
    )
    piece20= Outfit_Piece(
        piece_name='Nike Air Forces', 
        image='https://tinyurl.com/3vc3ta9z', 
        link='https://www.nike.com/t/air-force-1-07-mens-shoes-jBrhbr/CW2288-111?nikemt=true&cp=68540849105_search_--x-20301353919---c-----9019630-13071857-00194500874978&gclid=CjwKCAjwvfmoBhAwEiwAG2tqzJAnVg0eFLDQVxGg9POXtYl-t5djBuWDyi2g3OYIV1-UE7N-KpHHlRoCY-8QAvD_BwE&gclsrc=aw.ds', 
        piece_price=116.00,
        outfit_id=6
    )
    piece21 = Outfit_Piece(
        piece_name='Real Tree Wind Breaker', 
        image='https://www.sportsmans.com/medias/rustic-ridge-youth-realtree-zip-hunting-hoodie-realtree-edge-s-1503063-1.jpg?context=bWFzdGVyfGltYWdlc3wxNTU2ODZ8aW1hZ2UvanBlZ3xpbWFnZXMvaDcwL2g1Yy85NDEzNTExMTUxNjQ2LmpwZ3w0NmZmYTg5NDk1Y2MyMDBmZTQ0MGZkNTRiNDE0OWJmNTc5YTdiOGFlMzVmZDg0MWYyMDE3YzUzYjExNDdkYWFi', 
        link='https://www.sportsmans.com/clothing-outdoor-casual-men-women-youth/youth/hunting-fishing-clothing/rustic-ridge-youth-realtree-edge-zip-hunting-jacket/p/1503065?channel=shopping&gclid=CjwKCAjw4P6oBhBsEiwAKYVkq2gvEQBamVJzZr-gcWJtHoCnKmDFXlK7TwJYcS7GLC6BvLZofHoedBoCPhEQAvD_BwE', 
        piece_price= 19.99,
        outfit_id=7
    )
    piece22 = Outfit_Piece(
        piece_name='Brown corduroy pants', 
        image='https://image.goat.com/transform/v1/attachments/product_template_additional_pictures/images/062/992/408/original/784379_01.jpg.jpeg?action=crop&width=400', 
        link='https://www.llbean.com/llb/shop/119693?page=llbean-stretch-country-corduroy-pants-natural-fit-hidden-comfort-waist', 
        piece_price=70.95,
        outfit_id=7
    )
    piece23 = Outfit_Piece(
        piece_name='Brown Timbland', 
        image='https://images.timberland.com/is/image/timberland/A5VJN804-HERO?wid=650&hei=650&qlt=50&resMode=sharp2&op_usm=0.9,1.0,8,0', 
        link='https://www.timberland.com/en-us/p/featured-collections/50th-edition-collection-91606/mens-timberland-50th-anniversary-edition-premium-6-inch-waterproof-boot-TB0A5VJN804', 
        piece_price= 230.95,
        outfit_id=7
    )
    piece24 = Outfit_Piece(
        piece_name='Bucket Hat "BE CHANGE" - PEACE GANG', 
        image='https://i.pinimg.com/736x/66/10/8c/66108c3f66bfe2c0b0b5aff29cb69e5c.jpg', 
        link='https://peacegangworldwide.com/products/peace-gang-be-change-bucket-hat-1?variant=40078929559705', 
        piece_price= 34.99,
        outfit_id=8
    )
    piece25 = Outfit_Piece(
        piece_name='Carhartt Work In Progress prospector jacket in black', 
        image='https://img.shopstyle-cdn.com/sim/cc/64/cc6421519afe9c99f46ae577383f8d80_best/carhartt-wip-prospector-jacket-in-black.jpg', 
        link='https://www.shopstyle.com/g/men/carhartt-work-in-progress/prospector-jacket-in-black/939889319?utm_campaign=Pinterest_%22%22,ASOS&utm_medium=social&utm_source=Pinterest', 
        piece_price= 290.99,
        outfit_id=8
    )
    piece26 = Outfit_Piece(
        piece_name='Puma x Butter Goods Mens Lightweight Track Pants' , 
        image='https://img.shopstyle-cdn.com/sim/ba/c8/bac8beca65431f0852406b135d54d358_best/x-butter-goods-mens-lightweight-track-pants.jpg', 
        link='https://www.shopstyle.com/g/men/puma/x-butter-goods-mens-lightweight-track-pants/920461496?utm_campaign=Pinterest_%22%22,Neiman+Marcus&utm_medium=social&utm_source=Pinterest', 
        piece_price= 105.99,
        outfit_id=8
    )
    piece27 = Outfit_Piece(
        piece_name='Advbridge autumn', 
        image='https://advbridge.com/cdn/shop/products/Hefbe16f5da2e4f778fb46f64c0f289a1K.jpg?v=1670829562', 
        link='https://advbridge.com/products/advbridge-autumn-and-winter-sports-leisure-running-shoes-mens-shoes-air-cushion-shoes-shockproof-comfortable-tide-increase-thick-sol-1?variant=40914811584564', 
        piece_price= 71.44,
        outfit_id=8
    )











    db.session.add(piece1)
    db.session.add(piece2)
    db.session.add(piece3)
    db.session.add(piece4)
    db.session.add(piece5)
    db.session.add(piece6)
    db.session.add(piece7)
    db.session.add(piece8)
    db.session.add(piece9)
    db.session.add(piece10)
    db.session.add(piece11)
    db.session.add(piece12)
    db.session.add(piece13)
    db.session.add(piece14)
    db.session.add(piece15)
    db.session.add(piece16)
    db.session.add(piece17)
    db.session.add(piece18)
    db.session.add(piece19)
    db.session.add(piece20)
    db.session.add(piece21)
    db.session.add(piece22)
    db.session.add(piece23)
    db.session.add(piece24)
    db.session.add(piece25)
    db.session.add(piece26)
    db.session.add(piece27)
    
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_outfit_pieces():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.outfit_pieces RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM outfit_pieces;"))
        
    db.session.commit()