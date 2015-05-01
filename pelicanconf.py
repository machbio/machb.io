#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Sandeep Shantharam'
SITENAME = u'MachBio'
EMAIL_ADDRESS = u'machbio@gmail.com'
SITEURL = 'http://machb.io'
TIMEZONE = 'America/Indianapolis'
THEME = 'void/'
AVATAR = '/theme/images/avatar.jpg'
TITLE = " Sandeep Shantharam : Bioinformatics Student with Interests \
        in Data Analytics and Systems Biology "
DESCRIPTION = "Sandeep Shantharam is a Graduate Student interested  \
               in Biology, Internet and Everything related to Data Science "

# TODO: switch to /blog/slug/index.html -- need to setup redirects first
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Static Pages
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
#ABOUT_PAGE_HEADER = 'Nice to meet you.'

# DEFAULTS
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%b %d, %Y'
DEFAULT_PAGINATION = False

# FEEDS
FEED_ALL_ATOM = "feeds/all.atom.xml"
TAG_FEED_ATOM = "feeds/tag/%s.atom.xml"

# PLUGINS
PLUGIN_PATHS = ['pelican-plugins', 'pelican_dynamic']
PLUGINS = ['assets', 'liquid_tags.notebook', 'pelican_dynamic', 'render_math']

CODE_DIR = 'code'
NOTEBOOK_DIR = 'notebooks'
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

STATIC_PATHS = ['images', 'code', 'notebooks', 'extra']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},}

# TODO: NAVBAR - make it dynamic
NAVIGATION = [
    (),
]

# TODO: SOCIAL - make it dynamic
TWITTER_CARDS = True
TWITTER_NAME = "machbio"
GITHUB_NAME = 'machbio'
LINKEDIN_URL = 'http://linkedin.com/in/machbio'
GOOGLE_PLUS_URL = 'https://plus.google.com/+SandeepShantharam?rel=author'

#### Analytics
#GOOGLE_ANALYTICS = ''
DOMAIN = "machb.io"

# Other
MAILCHIMP = False
CACHE_CONTENT = False
AUTORELOAD_IGNORE_CACHE = True
