import sqlite3, sys
from tprint import tprint

class SQLite(object): 
    def __init__(self,db_path):
        self.conn = sqlite3.connect(db_path)
        tprint("Opened database successfully")
        self.curs = self.conn.cursor()
 
    def insert(self,sql):
        self.curs.execute(sql)
        # tprint("Data write in successfully")
        self.conn.commit()
        # self.conn.close()
 
    def select(self,sql):
        self.curs.execute(sql)
        # tprint("Data select successfully")
        res = self.curs.fetchall()
        # self.conn.close()
        return res
