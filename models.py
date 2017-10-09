from mongoengine import *
import datetime

_datetime = datetime.datetime


class AccessControlEntry(EmbeddedDocument):

    allow = BooleanField(required=True, default=True)
    securityID = StringField(required=True)
    orderID = IntField(required=True, default=1)
    whenCreated = DateTimeField(required=True, default=_datetime.now())

    meta = {
        'ordering': ['-orderID']
    }


class AuditPolicy(EmbeddedDocument):
    enableAuditing = BooleanField(required=True, default=True)
    ReadObject = BooleanField(required=True, default=False)
    ReadPassword = BooleanField(required=True, default=True)
    ChangePassword = BooleanField(required=True, default=True)
    ChangePasswordPolicy = BooleanField(required=True, default=True)
    ChangeObjectProperties = BooleanField(required=True, default=True)
    ChangeObjectACL = BooleanField(required=True, default=True)


class PasswordPolicy(EmbeddedDocument):

    passwordMinimumLength = IntField(required=True, default=15)
    passwordRequireSpecialChar = BooleanField(required=True, default=True)
    passwordRequireNumbers = BooleanField(required=True, default=True)
    passwordRequireLowerCaseChar = BooleanField(required=True, default=True)
    passwordRequireUpperCaseChar = BooleanField(required=True, default=True)
    passwordUseWhitespace = BooleanField(required=True, default=True)
    passwordMaximumAge = IntField(required=True, default=15)
    oneTimeUser = BooleanField(required=True, default=False)


class Environments(Document):

    displayName = StringField(required=True)
    accessControlEntries = EmbeddedDocumentListField(AccessControlEntry, required=True)
    whenCreated = DateTimeField(required=True, default=_datetime.now())


class Applications(Document):

    displayName = StringField(required=True)
    environmentID = ReferenceField(Environments, reverse_delete_rule=CASCADE)
    accessControlEntries = EmbeddedDocumentListField(AccessControlEntry, required=True)
    whenCreated = DateTimeField(required=True, default=_datetime.now())


class Groups(Document):

    displayName = StringField(required=True)
    applicationGroups = ListField(StringField(), required=False)
    applicationID = ReferenceField(Applications, reverse_delete_rule=CASCADE)
    accessControlEntries = EmbeddedDocumentListField(AccessControlEntry, required=True)
    whenCreated = DateTimeField(required=True, default=_datetime.now())


class Accounts(Document):

    displayName = StringField(required=True)
    userName = StringField(required=False)
    currentPassword = StringField(required=False)
    requiresChange = BooleanField(required=True, default=False)
    accessControlEntries = EmbeddedDocumentListField(AccessControlEntry, required=True)
    whenCreated = DateTimeField(required=True, default=_datetime.now())
    groupsID = ReferenceField(Groups, reverse_delete_rule=CASCADE)
