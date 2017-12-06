# coding: utf-8

try:
    from celery import shared_task
except ImportError:
    pass
