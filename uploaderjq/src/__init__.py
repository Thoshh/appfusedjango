#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# -------------------------------------------------------------------



__author__="aaloy"
__date__ ="$23/11/2008 15:59:18$"

import logging
import logging.config
from django.conf import settings

if settings.DEBUG:
    logging.basicConfig(level=logging.DEBUG, format="%(lineno)d %(asctime)s-%(name)s- %(message)s")
