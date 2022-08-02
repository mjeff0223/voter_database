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