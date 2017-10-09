import secrets
import string
from cryptography.fernet import Fernet
import os.path


class PasswordTools(object):

    def __init__(self, MinimumLength, RequireSpecialChar, RequireNumbers, RequireLowerCaseChar, RequireUpperCaseChar, RequireWhitespace):
        self.MinimumLength = MinimumLength
        self.RequireSpecialChar = RequireSpecialChar
        self.RequireNumbers = RequireNumbers
        self.RequireLowerCaseChar = RequireLowerCaseChar
        self.RequireUpperCaseChar = RequireUpperCaseChar
        self.UseWhitespace = RequireWhitespace

    def generatePassword(self):
        alphabet = ""

        if self.RequireNumbers:
            alphabet = alphabet + string.digits
        if self.RequireLowerCaseChar:
            alphabet = alphabet + string.ascii_lowercase
        if self.RequireUpperCaseChar:
            alphabet = alphabet + string.ascii_uppercase
        if self.RequireSpecialChar:
            alphabet = alphabet + '!@#$%^&*(){}[]<>?`~:;,.?'
        if self.RequireWhitespace:
            alphabet = alphabet + ' '

        password = ''.join(secrets.choice(alphabet) for i in range(self.MinimumLength))

        return password

    def generateKey (self, path):
        key = Fernet.generate_key().decode("utf-8")
        fullPath = os.path.join(path, "privacckey.key")
        file = open(fullPath, "w")
        file.write(key)
        file.close()

    def getKey (self, keyPath):
        file = open(keyPath, "rb")
        return file

    def encryptPassword(self, key, cleartextPassword):
        cipher = Fernet(key)
        bytes = cleartextPassword.encode()
        encryptedPassword = cipher.encrypt(bytes).decode("utf-8")
        return encryptedPassword
