from SMS.models import CustomUser
from .models import Code
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=CustomUser)
# This means each time CustomUser is created there should code generation
def code_generate(sender, instance, created, *args, **kwargs):
    if created:
        Code.objects.create(user=instance)
        