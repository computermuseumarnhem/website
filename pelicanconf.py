#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Computermuseum Hack42'
SITENAME = 'Computermuseum Hack42'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'nl'

LOCALE = 'en_GB.utf8'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'themes/museum'

MENUITEMS = [
    ('hack42.nl', 'https://hack42.nl/'),
]

INDEX_SAVE_AS = 'blog_index.html'

