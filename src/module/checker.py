import hashlib
import os

class Checker:
    
    def __init__(self):
        self.psw = os.environ.get('MAIL_PSW')
        self.digestor = hashlib.md5()

    def check( self, tmp ):
        self.digestor.update( tmp )
        tmp_h = self.digestor.hexdigest()
        self.digestor = hashlib.md5()
        return self.psw == tmp_h
