from flask import Blueprint, jsonify, abort, request
from ..models import Voter, Ballot, Account, db

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
