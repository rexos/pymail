from smtplib import SMTP, SMTPAuthenticationError
from getpass import getpass, getuser
import os
from sys import exit

SERVER = 'smtp.live.com'
PORT = 587

name = os.environ.get('MAIL_ADR')
if not name:
    name = raw_input('User : ')
psw = getpass()

server = SMTP( SERVER, port=PORT )
server.ehlo()
server.starttls()
server.ehlo()

try:
    server.login( name, psw )
except SMTPAuthenticationError:
    print('Wrong user or psw')
    sys.exit(0)
else:
    to = [ rcp.strip() for rcp in raw_input('To : ').split(',') ]
    msg = raw_input('Msg : ')
    failed = {}
    try:
        failed = server.sendmail( name, to, msg )
        server.close()
    except:
        print('Something went wrong, retry')
    else:
        if failed:
            print('Failed sending to ' + str(failed))
        else:
            print('Sent')
