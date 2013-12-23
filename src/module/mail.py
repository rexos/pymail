from smtplib import SMTP, SMTPAuthenticationError
import re

EMAIL_RE = '[-0-9a-zA-Z.+_]+@[-0-9a-zA-Z.+_]+\.[a-zA-Z]{2,4}'
SERVER = 'smtp.live.com'
PORT = 587

class Email:

    def __init__( self, name, psw ):
        self.name = name
        self.psw = psw
        self.to = [ rcp.strip() for rcp in re.findall( EMAIL_RE, raw_input('To : ') ) ]
        self.subject = "Subject : %s\n" % raw_input('Subject : ')
        self.msg = raw_input('Msg : ')
        self.footer = "\n\n----- sent from pymail -----"
        self.failed = {}

    def __str__( self ):
        return "From : " + self.name + "\nTo : " + \
            str(self.to) + "\n" + self.subject + "Body : " + self.msg
        
    def __start_server( self ):
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
                                                self.subject + self.msg + self.footer )
            self.server.close()
