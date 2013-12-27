from pysqlite2 import dbapi2 as db
import os
DBPATH = os.path.dirname( os.path.abspath( __file__ ) )
DBPATH = DBPATH+ '/../db/adr.sqlite'

def clean():
    if os.path.exists( DBPATH ):
        os.remove( DBPATH )

def main():
    clean()
    conn = db.connect( DBPATH )
    cur = conn.cursor()
    cur.execute( 'CREATE TABLE Addresses(' +
                 'id integer PRIMARY KEY AUTOINCREMENT,' + 
                 'address VARCHAR(30) UNIQUE NOT NULL,' + 
                 'alias VARCHAR(10) UNIQUE )')
    conn.commit()
    cur.execute( 'INSERT INTO Addresses(address, alias) VALUES("example@example.ex", "test")' )
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
