#-*- coding:utf-8 -*-

from os import mkdir
from os.path import join, lexists

from django.conf import settings
from django.core.management.commands import startapp

class Command(startapp.Command):
    def handle(self, app_name=None, target=None, **options):
        if target is None:
            target = join(settings.DJANGO_ROOT, 'apps', app_name)
            if lexists(target):
                raise ValueError(target + ' is already exists')
            else:
                mkdir(target)
        super(Command, self).handle(app_name, target, **options)
