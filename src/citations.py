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

def form_citations_list():
    citation_list = []
    if not session:
        return False
    
    citations = get_citations()

    for citation in citations:
        author = citation[1]
        title = citation[2]
        publisher = citation[3]
        year = citation[4]
        doi = citation[5]
        isbin = citation[6]
        editor = citation[7]
        pages = citation[8]
        shorthand = citation[9]
        section = [author, title, publisher, year, doi, isbin, editor, pages, shorthand]
        citation_list.append((add_section_to_citation(section), citation[0]))
    
    return citation_list

def add_section_to_citation(section):
    citation_text = ""
    if section[0] != None:
        citation_text += f"Kirjoittaja: {section[0]}"
    if section[1] != None:
        citation_text += f", Otsikko: {section[1]}"
    if section[2] != None:
        citation_text += f", Julkaisija: {section[2]}"
    if section[3] != None:
        citation_text += f", Vuosi: {section[3]}"
    if section[4] != None:
        citation_text += f", Doi: {section[4]}"
    if section[5] != None:
        citation_text += f", Isbin: {section[5]}"
    if section[6] != None:
        citation_text += f", Editor: {section[6]}"
    if section[7] != None:
        citation_text += f", Sivut: {section[7]}"
    if section[8] != None:
        citation_text += f", Shorthand: {section[8]}"
    
    
    return citation_text
            
