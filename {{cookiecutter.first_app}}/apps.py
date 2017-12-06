# coding: utf-8

from django.apps import AppConfig


class DefaultConfig(AppConfig):
    name = 'app_full'
    verbose_name = 'app_full'

    def ready(self):
        # импортировать сигналы для их регистрации
        from . import signals
