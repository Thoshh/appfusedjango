#!/bin/bash
echo "Actualitzant calaleg general"
pybabel extract -F babel.cfg -o agenda/locale/django.pot .
echo "Actualitzant idiomes"
pybabel update -D django -i agenda/locale/django.pot -d agenda/locale/
