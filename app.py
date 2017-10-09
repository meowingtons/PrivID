import falcon
from Resources import EnvironmentResource, ApplicationResource, GroupResource, AccountResource
from mongoengine import *

app = falcon.API()

connect(
    db='privacc',
    host='mongodb://localhost/privacc'
)

environment = EnvironmentResource()
application = ApplicationResource()
group = GroupResource()
account = AccountResource()

app.add_route('/environment', environment)
app.add_route('/application', application)
app.add_route('/group', group)
app.add_route('/account', account)
