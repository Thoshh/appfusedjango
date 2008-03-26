#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Data: 20:15:23
# Author: aaloy
# Description: Run all tests

import unittest
import testsuite

if __name__=="__main__":
    runner = unittest.TextTestRunner()
    runner.run(testsuite.suite)    
