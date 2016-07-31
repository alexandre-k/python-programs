from main import db
from models import BlogPost

# create the database and the db tables
db.create_all()

# insert
db.session.add(BlogPost('Good', 'So far I\'m good'))
db.session.add(BlogPost('Well', 'So far, everything goes well'))

# commit the changes
db.session.commit()
