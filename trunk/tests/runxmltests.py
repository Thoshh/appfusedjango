#!/usr/bin/env python
"Defines the unit tests for the application."
from  xmlrunner import XMLTestRunner
import testsuite
import sys


if __name__ == '__main__': 
    runner = XMLTestRunner(sys.stdout)
    runner.run(testsuite.suite)
