import pytest

class Person:
    def greet(self):
        return 'Hello, there!'

@pytest.fixture
def person():
    return Person()

def test_greet(person):
    greeting = person.greet()
    assert greeting == 'Hello, there!'
