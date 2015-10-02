"""
I don't exactly love that you have to do this.  I will look for a new design
"""
from apiwrappers import *
from dbwrappers import *
from nosqlwrappers import *
from consolewrappers import *
from alexawrappers import *
from hivewrappers import *
from elasticsearchwrappers import *
from liverailwrappers import *
import logging
try:
    from atlassianwrappers import *
except:
    logging.warning("missing dependencies for atlassianwrappers, ignoring...")
    pass
