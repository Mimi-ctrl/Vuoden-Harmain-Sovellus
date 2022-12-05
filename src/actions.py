from db import db
from os import getenv

def reset_database():
    
    if 'test' in getenv("DATABASE_URL"):
        from pathlib import Path
        try:
            sql = Path('../schema.sql').read_text()
            sql2 = "DELETE FROM users"
            db.session.execute(sql)
            db.session.commit()
            return True
        except:
            return False
    return False

