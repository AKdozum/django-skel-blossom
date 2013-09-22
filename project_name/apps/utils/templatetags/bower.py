#-*- coding:utf-8 -*-

from codecs import open
import json
import os
from os.path import join, isdir, exists

from django import template
register = template.Library()
from django.conf import settings

def get_min_pkg(main, ext):
    main_min = main.replace(ext, '.min' + ext)
    if exists(main_min):
        return main_min
    return main
BOWER_PKGS = {}
def get_pkg(pkg_name, ext):
    global BOWER_PKGS
    if pkg_name in BOWER_PKGS:
        return get_min_pkg(BOWER_PKGS[pkg_name], ext)
    for static_dir in settings.STATICFILES_DIRS:
        bower_dir = join(static_dir, 'bower', pkg_name)
        if not isdir(bower_dir): continue
        
        try:
            with open(join(bower_dir, 'bower.json'), mode='r', encoding='utf-8') as f:
                main = json.load(f)['main']
        except KeyError:
            continue
        pkg = settings.STATIC_URL + 'bower/' + pkg_name + '/' + main
        BOWER_PKGS[pkg_name] = pkg
        if main.endswith(ext):
            return get_min_pkg(pkg, ext)
    raise template.TemplateSyntaxError, "%s does not exist" % pkg_name

@register.simple_tag
def bower_css(pkg_name):
    pkg = get_pkg(pkg_name, '.css')
    return '<link rel="stylesheet" href="%s" type="text/css" charset="utf-8">' % pkg

@register.simple_tag
def bower_js(pkg_name):
    pkg = get_pkg(pkg_name, '.js')
    return '<script src="%s" charset="utf-8"></script>' % pkg
