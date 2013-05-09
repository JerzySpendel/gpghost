from django.db import models

class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.EmailField()
class Key(models.Model):
    ext_id = models.ForeignKey(User)
    key_id = models.CharField(max_length=1000)
    key_type = models.CharField(max_length=3)
    key_length = models.IntegerField()
    key_real = models.CharField(max_length=20)
    key_comment = models.CharField(max_length=250)
    key_email = models.EmailField()
    key_fingerprint = models.CharField(max_length=1000)
    key_password = models.CharField(max_length=1000)
    def isAlready(self):
        if Key.objects.filter(key_email=self.key_email).count() >= 1:
            return True
        else:
            return False


