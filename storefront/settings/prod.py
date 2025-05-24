import os
from common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['moshbuy-prod.herokuapp.com'] # All the hosts serving the app