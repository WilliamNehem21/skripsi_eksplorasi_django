from django.db import models
from django.utils.text import slugify
# Create your models here.
class Home(models.Model):
    nama = models.CharField(max_length=250)
    tanggal_lahir = models.DateField()
    slug = models.SlugField(blank=True, editable=False)

    def __str__ (self):
        return "{}".format(self.nama)
    
    def save(self):
        self.slug = slugify(self.nama)
        super(Home, self).save()

class Saran(models.Model):
    email = models.EmailField()
    saran = models.TextField()

    def __str__ (self):
        return "{}".format(self.email)