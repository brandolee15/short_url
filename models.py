from app import db

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_url = db.Column(db.String(100), index=True, unique=True)
    long_url = db.Column(db.String(200), index=True, unique=True)

    def __repr__(self):
        return '<URL {}>'.format(self.short_url)