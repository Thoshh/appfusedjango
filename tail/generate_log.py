#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: aaloy
# --------------------------------------------------------------------
# Propósito: generates the sample log
#---------------------------------------------------------------------
import time

arx = open('sample.log', 'w')
x = 0
while True:
    x = x+1
    arx.write("This is %s\n" % x)
    # just an small delay
    time.sleep(.5)
    arx.flush()
