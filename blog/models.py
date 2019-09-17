import re
from datetime import datetime
from blog import db


def slugify(s):
    regex = r'[^\w+]'
    return (re.sub(regex, '-', s)).lower()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(150), nullable=False, unique=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return 'Post id: {}, title: {}, date: {}'.format(self.id, self.title, self.date_posted)



