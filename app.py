import falcon
import config
from Resources import EnvironmentResource, ApplicationResource, GroupResource, AccountResource
from mongoengine import *

app = falcon.API()

connect(
    db=config.database_name,
    host=config.database_uri
)

environment = EnvironmentResource()
application = ApplicationResource()
group = GroupResource()
account = AccountResource()

app.add_route('/environment', environment)
app.add_route('/application', application)
app.add_route('/group', group)
app.add_route('/account', account)
