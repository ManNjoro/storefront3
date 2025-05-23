from rest_framework.test import APIClient
import pytest
from django.contrib.auth.models import User

@pytest.fixture(scope='session')
def django_db_setup():
    """Reuse the same DB across all tests in the session"""
    from django.test import override_settings
    override_settings(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        }
    )
@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def authenticate(api_client):
    def do_authenticate(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))
    return do_authenticate