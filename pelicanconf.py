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
CSS_FILE = 'main-6.css'

#sidebar links
EMAIL = 'heldergaray@gmail.com'
PHONE = '(+46) 0720258435'
WEBSITE = 'helderm.xyz'
LINKEDIN = 'helderm'
GITHUB = 'helderm'
TWITTER = '@heldergaray'

CAREER_SUMMARY = 'I am Machine Learning M.Sc. currently working as a data scientist at Booking.com. In the past I worked mostly as a backend engineer over a wide range of domains, like backend web applications, low-level drivers for custom hardware, authentication and job scheduling systems to name a few. My thesis topic was about detecting user abandoment behavior on Spotify using deep recurrent neural networks.'

SKILLS = [
	{
		'title': 'Python',
   		'level': '95'
   	},
  	{
  		'title': 'C / C++',
   		'level': '90'
   	},
    {
  		'title': 'Java',
  		'level': '80'
  	},
        {       'title': 'NoSQL DBs',
                'level': '80'
        },
        {       'title': 'ML Libs',
                'level': '90'
        },
        {       'title': 'Google Cloud',
                'level': '80'
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
		'details': 'At Booking.com I am working on understanding user behavior in the platform and also on its recommendation subsystem.'
	},
	{
		'job_title': 'Data Scientist (M.Sc. Internship)',
		'time': 'Jan 2017 - Aug 2017',
		'company': 'Spotify AB, Stockholm SE',
		'details': 'As a thesis project I studied churn prediction models to classify user abandonment on a music streaming service. State-of-the-art methods for this task like Logistic Regression and Random Forests were compared in terms of predictive power to a recurrent neural network called LSTM (Long Short-term Memory).'
	},
        {       'job_title': 'Software Developer (Summer Internship)',
                'time': 'Jun 2016 - Aug 2016',
                'company': 'Ericsson AB, Stockholm SE',
                'details': 'At Ericsson I researched and implemented tools for better development and deployment of Ericsson’s internal applications using Docker, Jenkins and an online Java IDE called Eclipse Che.'
        },
        {
                'job_title': 'Senior Software Engineer',
                'time': 'May 2012 - Jul 2015',
                'company': 'Terra Networks',
                'details': 'At Terra (www.terra.com.br), an online news portal in Latin America, I was the main developer responsible for the backend applications that rendered the website and stored user information. My main project was evolving the application from a static website to dynamically generated pages suited to the user\'s interest, while keeping the infrastructure scalable to the hardware available and the throughput of the website (100k reqs/sec). I also worked on identifying and blocking brute-force attacks on the authentication subsytem and maintaining a fault tolerant job scheduler system for importing news feeds into our databases.'
        },
        {
                'job_title': 'Software Engineer',
                'time': 'Feb 2010 - May 2012',
                'company': 'T&T Engineers (outsourced to Hewlett-Packard)',
                'details': 'At T&T I implemented the locality-optimized resource alignment algorithm for HP\'s Superdome 2 blade servers, an ANSI-C software that automatically allocates memory and CPU resources in a blade server as to minimize the physical distance between the components. I also maintained its command-line interface.'
        },
        {
                'job_title': 'Software Engineer',
                'time': 'Oct 2008 - Feb 2010',
                'company': 'CWI Software',
                'details': 'At CWI I developed RESTful APIs for online payments in ANSI-C, job schedulers in Java and a file system organizer for a DNS server in ANSI-C.'
        },
        {
                'job_title': 'Software Developer Intern',
                'time': 'Mar 2007 - Oct 2008',
                'company': 'Direcao Data Processing',
                'details': 'At Direcao I maintained and optimized a Point of Sale Terminal (POST) software in ANSI-C for supermarkets and retail stores.'
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
