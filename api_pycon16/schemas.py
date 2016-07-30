from flask_marshmallow import Marshmallow
from models import Puppy

ma = Marshmallow()

class PuppySchema(ma.Schema):
    class Meta:
        model = Puppy
        exclude = ['id', 'slug']

puppy_schema = PuppySchema()
puppies_schema = PuppySchema(many=True)
