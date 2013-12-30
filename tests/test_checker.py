import os
import sys
PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PATH + '/../src/module/')
from checker import Checker

class TestChecker( object ):
    def test_check( self ):
        chk = Checker()
        psw = 'correct_one'
        assert chk.check( psw ) == True
        assert chk.check( 'random_psw' ) == False
        
