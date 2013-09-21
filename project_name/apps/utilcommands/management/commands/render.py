# -*- coding: utf-8 -*-
import json
from codecs import open
from optparse import make_option
from django.core.management.base import BaseCommand
from django.template import Template, Context
from django.template.loader import render_to_string

def context_opt(option, opt_str, value, parser, *args, **kwargs):
    print value
    parser.values.context = json.loads(value)

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option("-c", "--context", default="{}",
                  action="store", type="string", dest="context"),
        )
    def handle(self, *args, **options):
        inputfile, outputfile = args
        out = render_to_string(inputfile, json.loads(options['context']))
        with open(outputfile, mode='w', encoding='utf-8') as f:
            f.write(out)
