class Email:
    
    def __init__( self, name ):
        self.frm = name
        self.to = [ rcp.strip() for rcp in raw_input('To : ').split(',') ]
        self.subject = "Subject : %s\n" % raw_input('Subject : ')
        self.msg = raw_input('Msg : ')
        self.failed = {}

    def __str__(self):
        return "From : " + self.frm + "To : " + str(self.to) + "\n" + self.subject + "Body : " + self.msg
        
    def send( self, server ):
        self.failed = server.sendmail( self.frm, self.to, self.subject + self.msg )
