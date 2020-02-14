from django.db import models


# Create your models here.
class Application(models.Model):
    club = models.CharField(max_length=2,
                            choices=[('uf', 'unifox'), ('em', 'emotion'),
                                     ('tl', 'teamlog'), ('l7', 'layer7'),
                                     ('tl', 'teamlog')])
    name = models.CharField(max_length=4, null=False)
    number = models.CharField(max_length=5, null=False)
    phone_number = models.CharField(max_length=11, null=False)
    email = models.EmailField(null=False)
    content = models.TextField(null=False, blank=True)
