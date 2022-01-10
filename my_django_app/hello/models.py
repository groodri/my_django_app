from django.db import models

# Create your models here.
def path_upload(instance, filename):
    var = filename.split('.')
    var_length = len(var) - 1
    var_extension = var[var_length]

    return "static/images/" + str(instance.id) + "." + var_extension


class Candidate(models.Model):
    name = models.CharField(max_length=50)
    surnames = models.CharField(max_length=50)
    signature = models.CharField(max_length=50, null=True, blank=True)
    degree = models.CharField(max_length=50, null=True, blank=True)
    university = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50)
    cv = models.FileField(null=True, blank=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)