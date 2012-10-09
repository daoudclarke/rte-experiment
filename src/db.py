# Bismillahi-r-Rahmani-r-Rahim
#
# Save entailment pairs to database

import sqlite3 as sqlite

class RteDb:
    def __init__(self, dbName):
        self.db = sqlite.connect(dbName)
        self.db.execute("CREATE TABLE EntailmentPairs (path VARCHAR, text VARCHAR, hypothesis VARCHAR, entailment INT)")
    
    def add(self, path, text, hypothesis, entailment):
        self.db.execute("INSERT INTO EntailmentPairs (path, text, hypothesis, entailment) VALUES")
    
    def close(self):
        self.db.commit()
        self.db.close()
                    
