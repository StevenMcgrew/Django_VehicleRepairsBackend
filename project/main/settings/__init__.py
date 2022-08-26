import os
from .base import *
# you need to set "vehicle_repairs_project = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
if os.environ.get('vehicle_repairs_project') == 'dev':
    from .dev import *
else:
    from .prod import *
