﻿#summary Starting a Django project
# Introduction #

This project goal is to create a minimun project that works but that goes beyond the Django tutorial.
That is, it will give you an scheleton that will allow you to create cruds operation, use of i18n, etc.

This is the first phase, playing a bit with Google subversion and defining the project. At this stage
it shows:

  * A basic project structure.
  * How to make a project developer independent, using a separated file to store the configuration.
  * Configuration to serve static media throught the Django server
  * Some simple views to show and edit a record
  * Use of pagination

## Last major updates ##

[26/06/2008] Added an example about how you can use jqgrid with Django. I have to adapt the js code a litte bit to use it with the json serializer that Django provides, but it's a minor change that in my oppinion corrects a bug in jqgrid.

![http://appfusedjango.googlecode.com/files/jqgrid_demo.jpg](http://appfusedjango.googlecode.com/files/jqgrid_demo.jpg)

For the minor ones just check the subversion

## Installation ##

  * Install the last Django svn.
  * Install sqlite libraries
  * Checkout the project
  * Copy properties.py.template to properties.py and cofigure it accornding your needs
  * run the server : python manage.py run server
  * point to http://localhost:8000/agenda

## Reference ##

  * Pagination styles: http://blog.localkinegrinds.com/2007/09/06/digg-style-pagination-in-django/
  * Django & Babel integration : http://babel.edgewall.org/wiki/BabelDjango
  * jqgrid : http://www.trirand.com/blog/