##!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Sources of inspiration:
# http://blog.panjiesw.com/posts/2014/04/static-blog-with-pelican/
# http://docs.getpelican.com/en/3.7.0/settings.html
# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3


from __future__ import unicode_literals

import hashlib
import os
import urllib


AUTHOR = 'Reece Hart'
AUTHOR_EMAIL = 'reece@harts.net'
BOOTSTRAP_THEME = "united"
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 5
DELETE_OUTPUT_DIRECTORY = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISQUS_SITENAME = "reeces-blog.disqus.com"  # disqus won't render in local dev mode
GITHUB_ACTIVITY_FEED = "https://github.com/reece.atom"
GITHUB_ACTIVITY_MAX_ENTRIES = 10
GITHUB_URL = 'http://github.com/reece/'
OUTPUT_RETENTION = [".hg", ".git", ".bzr"]
PATH = 'content'
PYGMENTS_STYLE = "friendly"
RELATIVE_URLS = True
SITENAME = "Reece's Blog"
SITEURL = "reece.github.io"
STATIC_PATHS = ['images']
TIMEZONE = 'America/Los_Angeles'
TWITTER_USERNAME = "reecehart"


# ARTICLE URLs
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}.html"
#ARTICLE_URL = ARTICLE_SAVE_AS
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'


# PLUGINS
PLUGIN_PATHS = [os.path.expanduser("~/opt/pelican-plugins")]
PLUGINS = ["code_include", "github_activity", "googleplus_comments", "gravatar", "tag_cloud", "i18n_subsites"]


# THEMES
# clean-blog, elegant, flex, pelican-twitchy, sundown
#THEME_PATH = os.path.expanduser('~/opt/pelican-themes/')
#THEME_NAME = "pelican-bootstrap3"
#THEME = os.path.join(THEME_PATH, THEME_NAME)
THEME = "./pelican-reecehart"


#JINJA_EXTENSIONS = ['jinja2.ext.i18n']
#JINJA_ENVIRONMENT = {'trim_blocks': True, 'lstrip_blocks': True}
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

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


# Conf for pulling Gravatar Image
GRV_SIZE = 120
DEFAULT_GRV_URL = u'http://www.example.com/default.jpg'
GRV_URL = "http://www.gravatar.com/avatar/" + hashlib.md5(AUTHOR_EMAIL.lower().encode("utf-8")).hexdigest() + "?"
GRV_URL += urllib.parse.urlencode({'d':DEFAULT_GRV_URL, 's':str(GRV_SIZE)})


