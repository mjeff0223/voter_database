"""
Populate twitter database with fake data using the SQLAlchemy ORM.
"""

import random
import string
import hashlib
import secrets
from faker import Faker

from voter.src.models import Account, Voter, Ballot, Candidate, District, Pac, pacs_voters, db
from voter.src import create_app

USER_COUNT = 50


# scramble password
def random_passhash():
    """Get hashed and salted password of length N | 8 <= N <= 15"""
    raw = ''.join(
        random.choices(
            string.ascii_letters + string.digits + '!@#$%&',  # valid pw characters
            k=random.randint(8, 15)  # length of pw
        )
    )

    salt = secrets.token_hex(16)

    return hashlib.sha512((raw + salt).encode('utf-8')).hexdigest()

# get party affiliation


def get_party():
    party = ['Democrat', 'Republican', 'Independent']
    party_choice = random.choice(party)
    return party_choice

# get candidate


def get_candidate():
    candidate = ['Dwayne Johnson', 'Andrew Yang', 'Lebron James']
    can_choice = random.choice(candidate)
    return can_choice


def get_pac():
    pac = ['End World Hunger',
           'Crypto For All',
           'Religious Freedom',
           'Freedom From Religion',
           'End all Wars']
    pac_choice = random.choice(pac)
    return pac_choice


def get_issue():
    issue = ['Social', 'Economic', 'Foreign Policy']
    issue_choice = random.choice(issue)
    return issue_choice


# def truncate_tables():
#     """Delete all rows from database tables"""
#     db.session.execute(likes_table.delete())
#     Tweet.query.delete()
#     User.query.delete()
#     db.session.commit()


def main():
    """Main driver function"""
    app = create_app()
    app.app_context().push()
    # truncate_tables()
    fake = Faker()

    last_voter = None
    for _ in range(USER_COUNT):
        last_voter = Voter(
            name=fake.unique.name(),
            age=random.randint(18, 80)
        )
        db.session.add(last_voter)

    db.session.commit()

    # last_user = None  # save last user
    # for _ in range(USER_COUNT):
    #     last_user = Account(
    #         username=fake.unique.first_name().lower() + str(random.randint(1, 150)),
    #         password=random_passhash(),
    #         party_affiliation=get_party(),
    #         voter_id=random.randint(1, 50)
    #     )

    #     db.session.add(last_user)

    # db.session.commit()

    # last_ballot = None  # save last user
    # for _ in range(USER_COUNT):
    #     last_ballot = Ballot(
    #     voter_id = random.randint(1,50),
    #     voted_for = get_candidate()
    #     )

    #     db.session.add(last_ballot)

    # db.session.commit()

    # last_candidate = None  # save last user
    # for _ in range(1,4):
    #     last_candidate = Candidate(
    #     candidate_name= get_candidate(),
    #     party = get_party()

    #     )
    #     db.session.add(last_candidate)

    # db.session.commit()

    # last_district = None  # save last user
    # for _ in range(USER_COUNT):
    #     last_district = District(
    #     state = fake.state(),
    #     voter_id = random.randint(1,50)
    #     )

    #     db.session.add(last_district)

    # db.session.commit()

    last_pac = None  # save last user
    for _ in range(50):
        last_pac = Pac(
            name=get_pac(),
            issue=get_issue(),
            voter_id=random.randint(1, 50)

        )
        db.session.add(last_pac)

    db.session.commit()

    pac_vote_pairs = set()
    while len(pac_vote_pairs) < 51:

        x = (
            random.randint(last_pac.id - USER_COUNT + 1, last_voter.id),
            random.randint(last_voter.id - USER_COUNT + 1, last_voter.id)
        )

        if x in pac_vote_pairs:
            continue  # pairs must be unique

        pac_vote_pairs.add(x)

    new_votes = [{"pac_id": pair[0], "voter_id": pair[1]}
                 for pair in list(pac_vote_pairs)]
    insert_votes_query = pacs_voters.insert().values(new_votes)
    db.session.execute(insert_votes_query)

    # insert likes
    db.session.commit()


main()
