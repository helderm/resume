#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Helder Martins'
SITENAME = u'helderm'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'

THEME = './themes/resume'

STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Theme configuration

#Profile information
NAME = 'Helder Martins'
TAGLINE = 'Data Scientist / Software Engineer'
PIC = 'profile.png'
CSS_FILE = 'main-3.css'

#sidebar links
EMAIL = 'heldergaray@gmail.com'
PHONE = '(+46) 0720258435'
WEBSITE = 'helderm.xyz'
LINKEDIN = 'helderm'
GITHUB = 'helderm'
TWITTER = '@heldergaray'

CAREER_SUMMARY = 'I am Machine Learning M.Sc. currently working as a data scientist at Booking.com. In the past I worked mostly as a backend engineer over a wide range of domains, like backend web applications, low-level drivers for custom hardware, authentication and job scheduling systems to name a few. My thesis topic was detecting user abandoment behavior on Spotify using deep recurrent neural networks.'

SKILLS = [
	{
		'title': 'Python',
   		'level': '95'
   	},
  	{
  		'title': 'C / C++',
   		'level': '80'
   	},
    {
  		'title': 'Java',
  		'level': '70'
  	}
]

PROJECT_INTRO = 'A list of projects I worked in the past.'

PROJECTS = [
	{
		'title': 'Songseeker',
		'tagline': 'Automatic playlist creator app for Android.'
	}
]

LANGUAGES = [
	{
		'name': 'Portuguese',
		'description': 'Native'
	},
	{
		'name': 'English',
		'description': 'Professional'
	},
	{
		'name': 'Spanish',
		'description': 'Amateur'
	}
]

INTERESTS = [
	'Games',
	'Footbal',
        'Travel'
]

EXPERIENCES = [
	{
		'job_title': 'Data Scientist',
		'time': 'Nov 2017 - Present',
		'company': 'Booking.com, Amsterdam NL',
		'details': 'Working on understanding user behavior in the platform and also on the recommendation system.'
	},
	{
		'job_title': 'Data Scientist (M.Sc. Internship)',
		'time': 'Jan 2017 - Aug 2017',
		'company': 'Spotify AB, Stockholm SE',
		'details': 'As a thesis project I studied churn prediction models to classify user abandonment on a music streaming service. State-of-the-art methods for this task like Logistic Regression and Random Forests were compared in terms of predictive power to a type of recurrent neural network called LSTM (Long Short-term Memory)'
	}
]

EDUCATIONS = [
	{
		'degree': 'M.Sc. Machine Learning',
		'meta': 'Royal Institute of Technology (KTH), Sweden',
		'time': '2015 - 2017'
	},
	{
		'degree': 'B.Sc. Computer Science ',
		'meta': 'Federal University of Rio Grande do Sul (UFRGS), Brazil',
		'time': '2004-2009'
	}
]
