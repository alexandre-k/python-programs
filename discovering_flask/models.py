from main import db

class BlogPost(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode, nullable=False)
    description = db.Column(db.Unicode, nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<title {}> <description {}>'.format(self.title, self.description)
