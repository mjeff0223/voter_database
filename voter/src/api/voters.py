from flask import Blueprint, jsonify, abort, request
from ..models import Voter, Ballot, Account, db

bp = Blueprint('voters', __name__, url_prefix='/voters')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    voters = Voter.query.all() # ORM performs SELECT query
    result = []
    for v in voters:
        result.append(v.serialize()) # build list of Voters as dictionaries
    return jsonify(result) # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    v = Voter.query.get_or_404(id)
    return jsonify(v.serialize())

@bp.route('', methods=['POST'])
def create():
    # req body must contain username and password
    if 'name' not in request.json or 'age' not in request.json:
        return abort(400)
    # construct Voter
    v = Voter(
        name=request.json['name'],
        age=request.json['age']
        
    )
    db.session.add(v) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(v.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    v = Voter.query.get_or_404(id)
    try:
        db.session.delete(v) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

