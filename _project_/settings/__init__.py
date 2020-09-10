from .global_settings import *
from .auth_settings import *
from .social_auth_settings import *

try:
    from .local_settings import *
except ImportError:
    pass
