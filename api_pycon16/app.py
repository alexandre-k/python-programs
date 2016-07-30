# In order to create a puppy with cUrl:
# curl -X POST 45.32.13.245:80 -d name=Lassie -d url=http://example.com/lassie.png -i
# To delete something
# curl -X DELETE 45.32.13.245:80/spot
# To identify yourself
# curl 45.32.13.245:80/whoami -H 'Authorization: <api_key>'
import sys
from flask import Flask, jsonify, abort, request, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Puppy, User
from slugify import slugify
from schemas import ma, puppy_schema
from flask_login import LoginManager, current_user, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///puppy.db'
db.init_app(app)
ma.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    if not api_key:
        return None
    return User.query.filter_by(api_key=api_key).first()

@app.route('/whoami')
def who_am_i():
    if current_user.is_authenticated:
        name = current_user.name
    else:
        name = 'anonymous'
    return jsonify({'name': name})

@app.route("/<slug>")
def get_puppy(slug):
    puppy = Puppy.query.filter(Puppy.slug==slug).first_or_404()
    return puppy_schema.jsonify(puppy)

@app.route("/", methods=["POST"])
@login_required
def create_puppy():
    # validate attributes
    puppy, errors = puppy_schema.load(request.form)
    if errors:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

    puppy.slug = slugify(puppy.name)
    db.session.add(puppy)
    db.session.commit()

    # return HTTP response
    resp = jsonify({'message': 'created'})
    resp.status_code = 201
    location = url_for('get_puppy', slug=slug)
    resp.headers['Location'] = location
    return resp

app.route('/<slug>', methods=['POST'])
def edit_puppy(slug):
    puppy = Puppy.query.filter(Puppy.slug==slug).first_org_404()
    puppy, errors = puppy_schema.load(request.form, instance=puppy)
    if errors:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

    puppy.slug = slugify(puppy.name)
    db.session.add(puppy)
    db.session.commit()

    resp = jsonify({'message': 'updated'})
    location = url_for(get_puppy, slug=puppy.slug)
    resp.headers['location'] = location
    return resp

@app.route('/<slug>', methods=['DELETE'])
def delete_puppy(slug):
    puppy = Puppy.query.filter(Puppy.slug==slug).first_org_404()
    db.session.delete(puppy)
    db.session.commit()
    return jsonify({'message': 'deleted'})

@app.errorhandler(404)
def page_not_found(error):
    resp = jsonify({'error': 'not found'})
    resp.status_code = 404
    return resp

@app.route('/', methods=['GET'])
def list_puppies():
    all_puppies = Puppy.query.all()
    data, errors = puppies_schema.dump(all_puppies)
    return jsonify(data)

if __name__ == "__main__":
    if 'createdb' in sys.argv:
        with app.app_context():
            db.create_all()
        print('Database created!')
    elif 'seeddb' in sys.argv:
        with app.app_context():
            p1 = Puppy(slug="rover", name="Rover",
                    image_url="http://example.com/rover.png")
            p2 = Puppy(slug='spot', name='spot',
                    image_url='http://example.com/spot.png')
            db.session.add(p1)
            db.session.add(p2)
            db.session.commit()
    else:
        app.run(host='0.0.0.0', port=80)

