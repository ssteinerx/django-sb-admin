# -*- coding: utf-8 -*-
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-sb-admin-ssx',
    version='0.4.0',
    packages=['django_sb_admin_ssx'],
    include_package_data=True,
    license='Apache License version 2.0',
    description='ssteinerX Version of SB Admin dashboard bootstrap 3 theme packaged as a reusable Django app.',
    long_description=README,
    url='https://github.com/ssteinerX/django-sb-admin',
    author='Steve Steiner',
    author_email='ssteinerX@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
)
