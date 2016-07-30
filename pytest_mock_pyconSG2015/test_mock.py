class DB:
    def __init__(self):
        pass

    def persist(self, person):
        pass

class Person:
    def __init__(self, name, db):
        self.name = name
        self.db = db

    def save(self):
        self.db.persist(self)

import pytest
from mock import Mock

@pytest.fixture
def mock_db():
    return Mock(spec=DB)

def test_save_persists_to_db(mock_db):
    gabe = Person('Gabe', mock_db)
    gabe.save()
    mock_db.persist.assert_called_with(gabe)
