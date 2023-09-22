from model import db

def login(username, password):
    user_rider = db.get_user(db.RIDERS_DB, username)
    user_passenger = db.get_user(db.PASSENGERS_DB, username)
    if (user_rider and user_rider[1] == password) or (user_passenger and user_passenger[1] == password):
        return True
    return False

def register_rider(username, password):
    try:
        db.add_rider(username, password)
        return True
    except:
        return False

def register_passenger(username, password):
    try:
        db.add_passenger(username, password)
        return True
    except:
        return False
