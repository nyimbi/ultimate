# coding: utf-8

from django.db.models import signals
from django.dispatch import receiver

from . import services, tasks
from . import models as m


#@receiver(signals.post_save, sender=Model)
#def signal_handler(sender, instance, created, **kwargs):
#    pass
