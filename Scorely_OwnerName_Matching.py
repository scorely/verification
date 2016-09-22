import nose
import coverage
import dedupe


#Sample of how it works

import unittest
from dedupe.variables.person import WesternPersonNameType

import numpy

class TestName(unittest.TestCase):

    def test_sounds_like_company(self) :
        name = WesternPersonNameType({'field' : 'foo'})
        distance = name.comparator('Goldman Sachs Co', 
                                   'Goldman, Sachs Co.')
        assert len(distance) == 65

def prettyPrint(variable, comparison) :
    for e in zip(variable.higher_vars, comparison) :
        print("%s:\t %s" % e)
        
        
        
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

from ._init import *

from dedupe.variables.name import WesternNameType

class WesternPersonNameType(WesternNameType):
    type = "Person Name"

    def __init__(self, definition) :
        definition['name type'] = 'person'

        super(WesternPersonNameType, self).__init__(definition)