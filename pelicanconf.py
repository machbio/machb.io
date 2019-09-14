#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Sandeep Shantharam'
SITENAME = u'MachBio'
EMAIL_ADDRESS = u'machbio@gmail.com'
SITEURL = 'http://machb.io'
TIMEZONE = 'America/Indiana/Indianapolis'
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
PLUGINS = ['assets', 'liquid_tags.notebook', 'pelican_dynamic', 'render_math', \
			'neighbors', 'pelican_gist', 'tipue_search', 'sitemap']

CODE_DIR = 'code'
NOTEBOOK_DIR = 'notebooks'
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

STATIC_PATHS = ['images', 'code', 'notebooks', 'extra', 'admin']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},}
MATH_JAX = {'color':'blue','align': 'center'}

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
DISQUS_SITENAME = "machbio"

RELATIVE_URLS = True
#TAG_URL = 'tags/tag-{slug}.html'
#TAG_SAVE_AS = 'tags/tag-{slug}.html'
TAGS_URL = 'tags.html'
TAGS_SAVE_AS = 'tags.html'
#ARCHIVES_URL = 'archives.html'
#ARCHIVES_SAVE_AS = 'archives.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'

# Tipue Search
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

TEMPLATE_PAGES = {'admin/index.html': 'admin/index.html'}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
