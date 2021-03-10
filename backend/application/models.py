from django.db import models
from django.contrib import admin


# Create your models here.
class Application(models.Model):
    club = models.CharField(max_length=2,
                            choices=[('uf', 'unifox'), ('em', 'emotion'),
                                     ('tl', 'teamlog'), ('l7', 'layer7'),
                                     ('nf', 'nefus')])
    name = models.TextField(null=False, blank=False)
    number = models.TextField(null=False, blank=False)
    phone_number = models.TextField(null=False, blank=False)
    email = models.EmailField(null=False)
    content = models.TextField(null=False, blank=True)
    is_hide = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)