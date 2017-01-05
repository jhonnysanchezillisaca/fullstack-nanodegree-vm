from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

myFirstRestaurant = Restaurant(name='Pizza Palace')
session.add(myFirstRestaurant)
session.commit()

# items = session.query(MenuItem).all()
# for item in items:
#     print item.name

veggieBurguers = session.query(MenuItem).filter_by(name="Veggie Burger")
for veggieBurguer in veggieBurguers:
    print veggieBurguer.id
    print veggieBurguer.price
    print veggieBurguer.restaurant.name
    print "\n"
