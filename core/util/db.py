from lib.db import db

def execute(query, params=None):
    cursor = db.cursor()
    cursor.execute(query, params)
    db.commit()
    cursor.close()
    return True

def fetch_one(query, params=None):
    cursor = db.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()
    cursor.close()
    return result

def fetch_all(query, params=None):
    cursor = db.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    return result

