# modules/__init__.py
# Automatically import all modules so they can be used in main.py

from . import domain_lookup
from . import ip_info
from . import email_search
from . import social_media_search
from . import search_phone_number
from . import data_breach_search
from . import people_search
from . import image_lookup
from . import image_metadata_lookup
from . import email_internet_search

# Optional: define what gets imported with 'from modules import *'
__all__ = [
    "domain_lookup", "ip_info", "email_search", "social_media_search",
    "search_phone_number", "data_breach_search", "people_search",
    "image_lookup", "image_metadata_lookup", "email_internet_search"
]