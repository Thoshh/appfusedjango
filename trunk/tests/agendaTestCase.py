import unittest
import sys
sys.path.append('..')
from agenda.models import Person, Diari


class NotImplementedException(Exception):
    
    def __init__(self, value="Not implemented"):
        self.value=value
        Exception.__init__(self)
                
    def __str__(self):
        return repr(self.value)

class AgendaTestCase(unittest.TestCase):
    def setup(self):
        persones = Person.objects.all()
        diaris = Diaris.objects.all()
        
    def tearDown(self):
        pass
    def testAddPerson(self):
        raise NotImplementedException()
    
    def testAddDiari(self):
        raise NotImplementedException()
    
    def testDeletePerson(self):
        raise NotImplementedException()

def agendaTestSuite():
    return unittest.TestLoader().loadTestsFromTestCase(AgendaTestCase)
        