from typing import Optional

class DatabaseConnection:
    _instance:Optional['DatabaseConnection']=None
    _connection = None
    
    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection,cls).__new__(cls)
        return cls._instance
    
    def _connect(self)->None:
        print('Database Connection Established')
        self._connection = True
    
    def get_connection(self)->None:
        if self._connection is None:
            self._connect()
            return
        print('Database Connection Already Exists')
    
    def close(self)->None:
        print('Database Connection Closed Successfully')
        self._connection = False

# Client Code

db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1)
print(db2)
print(db1==db2)
db1.get_connection()
db2.get_connection()