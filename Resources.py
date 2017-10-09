import falcon
from models import *


class EnvironmentResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = Environments.objects.to_json()


class ApplicationResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = Applications.objects.to_json()


class GroupResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = Applications.objects.to_json()


class AccountResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = Accounts.objects.to_json()