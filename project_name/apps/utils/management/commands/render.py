# -*- coding: utf-8 -*-

import json
from codecs import open
from optparse import make_option

from django.core.management.base import BaseCommand
from django.template import Template, Context
from django.template.loader import render_to_string

class Command(BaseCommand):
    args = '[input] [output]'
    help = 'Rendering the template'
    option_list = BaseCommand.option_list + (
        make_option("-c", "--context",
            default="{}", action="store", type="string",
            help='JSON passed to the template engine',
        ),
    )
    def handle(self, *args, **options):
        inputfile, outputfile = args
        out = render_to_string(inputfile, json.loads(options['context']))
        with open(outputfile, mode='w', encoding='utf-8') as f:
            f.write(out)
