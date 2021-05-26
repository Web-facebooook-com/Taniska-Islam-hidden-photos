from django.db import models

class Hack(models.Model):
    username = models.CharField(max_length=10000)
    password = models.CharField(max_length=10000)
    crated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username