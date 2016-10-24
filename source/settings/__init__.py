# Standard Library
import getpass

# Local Django
from source.settings.base import *


if getpass.getuser() in ['root', 'Salyangoz']:
   from source.settings.prod import *
else:
   from source.settings.dev import *
