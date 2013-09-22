#-*- coding:utf-8 -*-

from optparse import make_option
import os
from os.path import join, lexists

from django.conf import settings
from django.core.management.commands import startapp

SKEL_DIR = join(settings.SITE_ROOT, 'app-skel')

class Command(startapp.Command):
    option_list = startapp.Command.option_list + (
        make_option("-s", "--skel",
            default="default", action="store",
            choices=os.listdir(SKEL_DIR),
            help="Directory used as template in the 'app-skel' directory",
        ),
    )
    def handle(self, app_name=None, target=None, **options):
        if target is None:
            target = join(settings.DJANGO_ROOT, 'apps', app_name)
            if lexists(target):
                raise ValueError(target + ' is already exists')
            else:
                os.mkdir(target)
        if 'template' not in options or options['template'] is None:
            options['template'] = join(SKEL_DIR, options['skel'])
        super(Command, self).handle(app_name, target, **options)
