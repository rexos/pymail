from pysqlite2 import dbapi2 as db
import os
DBPATH = os.path.dirname( os.path.abspath( __file__ ) )
DBPATH = DBPATH + '/../db/adr.sqlite'

class Book():
    def __init__( self ):
        conn = db.connect( DBPATH )
        self.cursor = conn.cursor()

    def __wrap( self, pattern ):
        return '%' + pattern + '%'

    def lookup( self, pattern ):
        self.cursor.execute( 'SELECT * FROM Addresses WHERE ' +
                             'address LIKE ? OR alias LIKE ?',
                             ( self.__wrap( pattern ), 
                               self.__wrap( pattern ), ) )
        print( self.cursor.fetchone() )

    def insert( self, address, alias ):
        self.cursor.execute( 'INSERT INTO Addresses(address, alias) ' +
                             'VALUES(?, ?)', (address, alias,) )

    def close( self ):
        conn = self.cursor.connection()
        conn.close()
