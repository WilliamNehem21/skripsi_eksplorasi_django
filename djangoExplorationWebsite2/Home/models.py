from django.db import models

# Create your models here.
class Home(models.Model):
    nama = models.CharField(max_length=250)
    tanggal_lahir = models.DateField()

    def __str__ (self):
        return "{}".format(self.nama)