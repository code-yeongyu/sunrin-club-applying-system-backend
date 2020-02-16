from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    club = models.CharField(max_length=2,
                            choices=[('uf', 'unifox'), ('em', 'emotion'),
                                     ('tl', 'teamlog'), ('l7', 'layer7'),
                                     ('nf', 'nefus')])
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                unique=True)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()