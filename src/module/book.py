from pysqlite2 import dbapi2 as db
import os
import re
DBPATH = os.path.dirname( os.path.abspath( __file__ ) )
DBPATH = DBPATH + '/../db/adr.sqlite'

EMAIL_RE = '[-0-9a-zA-Z.+_]+@[-0-9a-zA-Z.+_]+\.[a-zA-Z]{2,4}'

class Book():
    def __init__( self ):
        conn = db.connect( DBPATH )
        self.cursor = conn.cursor()

    def __wrap( self, pattern ):
        return '%' + pattern + '%'

    def __isemail( self, ptr ):
        adr = re.findall( EMAIL_RE, ptr )
        if adr != []:
            alias = raw_input('Alias : ')
            self.insert( adr[0], alias )
            return adr[0]
        else:
            return None

    def get_to( self ):
        adr = raw_input('To : ')
        fnd = self.__isemail( adr )
        while not fnd:
            to = self.lookup( adr )
            if to:
                break
            adr = raw_input('To : ')
        return fnd if fnd else to[1]

    def lookup( self, pattern ):
        self.cursor.execute( 'SELECT * FROM Addresses WHERE ' +
                             'address LIKE ? OR alias LIKE ?',
                             ( self.__wrap( pattern ), 
                               self.__wrap( pattern ), ) )
        return self.cursor.fetchone()

    def insert( self, address, alias ):
        self.cursor.execute( 'INSERT INTO Addresses(address, alias) ' +
                             'VALUES(?, ?)', (address, alias,) )
        self.cursor.connection.commit()
        
    def close( self ):
        self.cursor.connection.conn.close()
