import psycopg2


#####################################################################################
#PostgreSQL
database = "dbname=yajing_nlp"
user = "user=yajing"

class db_handler:
    def __init__(self,db=database,ur=user):
        self.db = db
        self.user = ur
        self.conn = 0
        self.cursor = 0
        self.connect()
        self.get_cursor()
    def __exit__(self,type,value,traceback):
        self.close()        
    def connect(self):
        self.conn = psycopg2.connect(self.db+" "+self.user)
    def close(self):
        self.cursor.close() #modify later
        self.conn.close()
    def get_cursor(self):
        self.cursor = self.conn.cursor()
    def fetchone(self):
        return self.cursor.fetchone()
    def fetchall(self):
        return self.cursor.fetchall()        
    def execute(self,command,value = None):
        if value == None:
          self.cursor.execute(command)
        else:
          self.cursor.execute(command,value)
    def commit(self):
        self.conn.commit()
#####################################################################################
