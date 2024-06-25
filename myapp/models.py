from django.db import models

class TotalAssault(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class GrandAssault(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name