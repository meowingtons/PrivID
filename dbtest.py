from mongoengine import *
from models import *
import datetime

connect(
    db='privacc',
    host='mongodb://localhost/privacc'
)

accessControlEntry = AccessControlEntry()
accessControlEntry.securityID = "testSecurityID"

environment = Environments()
environment.displayName = "Test Environment"
environment.accessControlEntries = [accessControlEntry]
environment.whenCreated = datetime.datetime.now()
environment.save()
