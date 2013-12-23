import os
import sys

PATH = os.path.dirname( os.path.abspath( __file__ ) )
sys.path.insert( 0, PATH + '/module' )

from getpass import getpass, getuser
from checker import Checker
from mail import Email

name = os.environ.get('PYMAIL_ADR')
if not name:
    name = raw_input('User : ')

chk = Checker()
psw = getpass()
while not chk.check( psw ):
    print('Sorry .. retry')
    psw = getpass()

try:
    e = Email( name, psw )
    try:
        e.send()
    except:
        print('\nSomething went wrong, retry')
    else:
        if e.failed:
            print('Failed sending to ' + str(e.failed))
        else:
            print('Sent')
except KeyboardInterrupt:
    print('\nTerminated')
    sys.exit(0)
