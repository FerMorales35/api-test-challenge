import pytest
from pages.import_api import ImportAPi

@pytest.fixture(scope="session")
def base_url():
    return "https://api.test.worldsys.ar"

@pytest.fixture(scope="session")
def token():
    return "XXX" #Completar con el token correcto

@pytest.fixture
def person_id():
    return 111

@pytest.fixture
def api(base_url, token):
    return ImportAPi(base_url, token)