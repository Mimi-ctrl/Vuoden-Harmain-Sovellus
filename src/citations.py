from db import db
from flask import session

def add_citation(author, title, year):
    if not session or title == "" or not year.isdigit():
        return False
    user_id = session.get("user_id")
    try:
        sql = "INSERT INTO entries (author, title, year, user_id) VALUES (:author, :title, :year, :user_id)"
        db.session.execute(sql, {"author":author, "title":title, "year":year, "user_id":user_id})
        db.session.commit()
        return True
    except:
        return False
    
def get_citations():
    if not session:
        return False
    user_id = session.get("user_id")
    try:
        sql = "SELECT * FROM entries WHERE user_id=:user_id"
        result = db.session.execute(sql, {"user_id":user_id})
        return result.fetchall()
    except:
        return False

def delete_citation(id):
    if not session:
        return False
    try:
        sql = "DELETE FROM entries WHERE id=:id"
        db.session.execute(sql, {"id":id})
        db.session.commit()
        return True
    except:
        return False