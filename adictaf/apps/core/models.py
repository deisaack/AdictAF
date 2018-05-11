from django.db import models
from adictaf.utilities.crypto import SafiCrypto

class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=300, blank=True)

    def set_password(self, password):
        s=SafiCrypto()
        pwd=s.make_token(password)
        self.password = pwd
        self.save()

    def get_password(self):
        s=SafiCrypto()
        pwd=s.decode_token(self.password)
        return pwd

    def check_password(self, password):
        return self.get_password() == password

