#!/bin/bash
# First we must create the global file
pybabel extract -F babel.cfg -o agenda/locale/django.pot .
# then de different languages
pybabel init -D django -i agenda/locale/django.pot -d agenda/locale -l ca
pybabel init -D django -i agenda/locale/django.pot -d agenda/locale -l es
pybabel init -D django -i agenda/locale/django.pot -d agenda/locale -l en
