from smtplib import SMTP, SMTPAuthenticationError, SMTP_SSL
import re
import os
import sys
from book import *

SERVER = os.environ.get( 'PYMAIL_SRV' )
PORT = os.environ.get( 'PYMAIL_PRT' )
SSL = os.environ.get( 'PYMAIL_SSL' )

class Email:

    def __init__( self, name, psw ):
        self.book = Book()
        self.name = name
        self.psw = psw
        self.to = self.book.get_to()
        self.subject = 'Subject : %s\n' % raw_input('Subject : ')
        self.msg = raw_input('Msg : ')
        self.failed = {}

    def __str__( self ):
        return 'From : ' + self.name + '\nTo : ' + \
            str(self.to) + '\n' + self.subject + 'Body : ' + self.msg
        
    def __start_server( self ):
        if SSL:
            self.server = SMTP_SSL( SERVER, port=PORT )
        else:
            self.server = SMTP( SERVER, port=PORT )
            self.server.ehlo()
            self.server.starttls()

        self.server.ehlo()

    def send( self ):
        self.__start_server()
        try:
            self.server.login( self.name, self.psw )
        except SMTPAuthenticationError:
            print('Wrong user or psw')
            sys.exit(0)
        else:
            self.failed = self.server.sendmail( self.name, self.to,
                                                self.subject + self.msg )
            self.server.close()
