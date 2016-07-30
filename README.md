===============
django-sb-admin-ssx
===================

Introduction
------------

I (ssteinerX) added the -ssx suffix to distinguish this from the original
Django port refrenced below.

Django SB Admin is a resuable Django app which provides a Bootstrap 3 SB Admin dashboard theme.

Forked by ssteinerX from:

    https://github.com/bluszcz/django-sb-admin
    http://startbootstrap.com/template-overviews/sb-admin/

SB Admin is a free to download Bootstrap admin template. This template uses the
default Bootstrap 3 styles along with a variety of powerful jQuery plugins to
create a powerful framework for creating admin panels, web apps, or back-end dashboards.

Note: July 6, 2016
------------------

I (ssteinerX) have picked up development of this for a project I'm currently working on.  I'll submit pull requests to the original project to see whether bluszcz is interested in continuing development, but since it's not been touched since November 2015, I'm not sure whether he'll be interested in my changes.  I will make sure to make atomic pull requests for little bug fixes and/or deprecation removals, but my focus is on Django 1.10 so, without any automated tests at this point, I'm not particularly worried about backwards compatibility.

    https://github.com/ssteinerx/django-sb-admin

I will also be upgrading bootstrap etc. and rearranging a bit for improved future updates with Bower and Gulp instead of error prone manual copying into the project.

Please feel free to fork, submit pull requests, or add issues here.

Installation
------------

1. Install an app::

    pip install django-sb-admin_ssx

2. Add "django_sb_admin_ssx" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'django_sb_admin_ssx',
    )

3. If you want to see an example app, add following to your urls file::

    import django_sb_admin_ssx.urls

    url(r'^django-sb-admin_ssx/', include(django_sb_admin_ssx.urls.urlpatterns)),

Usage
-----

1. Copy following blank template::

    django_sb_admin_ssx/sb_admin_blank.html

or:

2. Extend a base template::

    {% extends "django_sb_admin_ssx/base.html" %}

and then:

3. Override following blocks::

    {% block sb_admin_header %}<!-- Header of the page -->{% endblock sb_admin_header %}
    {% block sb_admin_title %}<!-- Title of the content the page -->{% endblock sb_admin_title %}
    {% block sb_admin_sidebar %}<!-- left sidebar -->{% endblock sb_admin_sidebar %}
    {% block sb_admin_navbar_right %}<!-- right top navbar -->{% endblock sb_admin_navbar_right %}
    {% block sb_admin_content %}<!-- content -->{% endblock sb_admin_content %}

To use included login page put following in your **urls.py**::

    url(r'^accounts/login/$', auth_views.login,
        {'template_name': 'django_sb_admin_ssx/examples/login.html'}),


Conventions
-----------

Template blocks
===============

* Names  of blocks start with *sb_admin*

Extras
------

* login template
* messages support in a base template

License
-------

Copyright 2015 Rafal Zawadzki

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

SB Admin itself is licensed under the Apache License
https://github.com/IronSummitMedia/startbootstrap-sb-admin/blob/gh-pages/LICENSE
