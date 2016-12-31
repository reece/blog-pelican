##!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Sources of inspiration:
# http://blog.panjiesw.com/posts/2014/04/static-blog-with-pelican/


from __future__ import unicode_literals

import hashlib
import os
import urllib


#MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}.html"
ARTICLE_URL =     ARTICLE_SAVE_AS
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

RELATIVE_URLS = True

AUTHOR = 'Reece Hart'
AUTHOR_EMAIL = 'reece@harts.net'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
PATH = 'content'
SITENAME = 'Reece Hart'
#SITEURL = ''
STATIC_PATHS = ['images']
TIMEZONE = 'America/Los_Angeles'

GITHUB_URL = 'http://github.com/reece/'
TWITTER_USERNAME = "reecehart"

LINKS = ()

SOCIAL = (
    ('BitBucket',      'https://bitbucket.org/reece'),
    ('Facebook',       'https://www.facebook.com/reece.k.hart'),
    ('GitHub',         'https://github.com/reece'),
    ('Google Plus',    'https://plus.google.com/+ReeceHart'),
    ('LinkedIn',       'https://linkedin.com/in/reece'),
    ('Stack Overflow', 'http://stackoverflow.com/users/342839/reece'),
    ('Twitter',        'https://twitter.com/reecehart'),
)


# THEME_PATH = os.path.expanduser('~/opt/pelican-themes/')
# THEME = THEME_PATH + "sundown"
# clean-blog
# elegant
# flex
# pelican-twitchy
# sundown
THEME = "./theme"

# Conf for pulling Gravatar Image
GRV_SIZE = 120
DEFAULT_GRV_URL = u'http://www.example.com/default.jpg'
GRV_URL = "http://www.gravatar.com/avatar/" + hashlib.md5(AUTHOR_EMAIL.lower().encode("utf-8")).hexdigest() + "?"
GRV_URL += urllib.parse.urlencode({'d':DEFAULT_GRV_URL, 's':str(GRV_SIZE)})
