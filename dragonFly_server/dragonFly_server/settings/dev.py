from .common import *
from corsheaders.defaults import default_headers

INTERNAL_IPS = ["127.0.0.1"]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]