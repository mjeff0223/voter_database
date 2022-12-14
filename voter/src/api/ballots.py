from flask import Blueprint, jsonify, abort, request
from ..models import Voter, Ballot, Account, db

bp = Blueprint('ballots', __name__, url_prefix='/ballots')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    ballots = Ballot.query.all()  # ORM performs SELECT query
    result = []
    for b in ballots:
        result.append(b.serialize())  # build list of Voters as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    b = Ballot.query.get_or_404(id)
    return jsonify(b.serialize())
