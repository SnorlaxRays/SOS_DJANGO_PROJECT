
from SOS_DJANGO_PROJECT.settings import EMAIL_HOST_USER

class EmailMessage:

    def __init__(self):
        self.frm = EMAIL_HOST_USER
        self.to = []
        self.cc = []
        self.bcc = []
        self.subject = ""
        self.text = ""
        self.type = "html"
        self.attachment = []
