import pytest

from employ import Employ

@pytest.fixture
def person_object():
    '''create an object of the employ class that will be used by all test funtion'''
    person1 = Employ('prince','nyambe',4500)
    return person1

def test_give_default_raise(person_object):
    '''test if give_riase method works without passing it any arguments'''
    person1 = person_object
    person1.give_raise()
    assert person1.annual_salary == (4500+5000)

def test_give_custom_raise(person_object):
    '''test if give_raise method works when passed an argument'''
    person1 = person_object
    person1.give_raise(580)
    assert person1.annual_salary == 5080
