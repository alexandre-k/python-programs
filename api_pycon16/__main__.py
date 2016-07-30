from models import *
from app import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///puppy.db'
db.init_app(app)

p1 = Puppy(slug="rover", name="Rover",
        image_url="http://example.com/rover.png")
p2 = Puppy(slug='spot', name='spot',
        image_url='http://example.com/spot.png')

db.session.add(p1)
db.session.add(p2)

db.session.commit()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

