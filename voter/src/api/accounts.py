from random import randint
from flask import Blueprint, jsonify, abort, request
from ..models import Voter, Ballot, Account, db
import hashlib
import secrets
import random


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('accounts', __name__, url_prefix='/accounts')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    accounts = Account.query.all()  # ORM performs SELECT query
    result = []
    for a in accounts:
        result.append(a.serialize())  # build list of Voters as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    a = Account.query.get_or_404(id)
    return jsonify(a.serialize())


@bp.route('', methods=['POST'])
def create():
    # req body must contain username and password
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    # username must be at least 3 characters and password must be at least 8 characters
    if len(request.json['username']) < 3 or len(request.json['password']) < 12:
        return abort(400)
    # construct User
    a = Account(
        username=request.json['username'],
        password=scramble(request.json['password']),
        party_affiliation=(request.json['party_affliation']),
        voter_id=(request.json['voter_id'])
    )
    db.session.add(a)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(a.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    a = Account.query.get_or_404(id)
    try:
        db.session.delete(a)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id):
    a = Account.query.get_or_404(id)
    if 'username' not in request.json and 'password' not in request.json and 'party_affiliation' not in request.json:
        return abort(400)
    if 'username' in request.json:
        if len(request.json['username']) >= 3:
            a.username = request.json['username']
        else:
            return abort(400)

    if 'password' in request.json:
        if len(request.json['password']) >= 8:
            a.password = scramble(request.json['password'])
        else:
            return abort(400)

    if 'party_affiliation' in request.json:
        a.party_affiliation = request.json['party_affiliation']

    try:
        db.session.commit()
        return jsonify(a.serialize())
    except:
        return jsonify(False)
