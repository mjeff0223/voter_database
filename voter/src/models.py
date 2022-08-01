from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()


class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    party_affiliation = db.Column(db.String(128), nullable=False)
    voter_id = db.Column(db.Integer, db.ForeignKey(
        'voters.id'), nullable=False)


class Ballot(db.Model):
    __tablename__ = 'ballots'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    voter_id = db.Column(db.Integer, db.ForeignKey(
        'voters.id'), nullable=False)
    voted_for = db.Column(db.String(128), nullable=False)
    voted_on = db.Column(db.DateTime,
                         default=datetime.datetime.utcnow,
                         )

    def __init__(self, voter_id: int, voted_for: str):
        self.voter_id = voter_id
        self.voter_for= voted_for
        

    def serialize(self):
        return {
            'id': self.id,
            'voter_id' : self.voter_id,
            'voted_for' : self.voted_for,
            'voted_on': self.voted_on.isoformat()
        }


class Candidate(db.Model):
    __tablename__ = 'candidates'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidate_name = db.Column(db.String(128), nullable=False)
    party = db.Column(db.String(128))


class District(db.Model):
    __tablename__ = 'districts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state = db.Column(db.String(128))
    voter_id = db.Column(db.Integer, db.ForeignKey(
        'voters.id'), nullable=False)


class Pac(db.Model):
    __tablename__ = 'pacs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    issue = db.Column(db.String(128))
    voter_id = db.Column(db.Integer, db.ForeignKey(
        'voters.id'), nullable=False)


pacs_voters = db.Table(
    'pacs_voters',
    db.Column(
        'voter_id', db.Integer,
        db.ForeignKey('voters.id'),
        primary_key=True
    ),
    db.Column(
        'pac_id', db.Integer,
        db.ForeignKey('pacs.id'),
        primary_key=True
    ),

)


class Voter(db.Model):
    __tablename__ = 'voters'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name: str, voter_id: int, age: int):
        self.name = name
        self.voter_id = voter_id
        self.age = age

    def serialize(self):
        return {
            'id': self.id,
            'name' : self.name,
            'age': self.age
        }

    