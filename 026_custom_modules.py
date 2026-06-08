# We can ue any .py file as custom module
# For this purposes we should import whole file a module or it method a written below

import resources.module as module
from resources.module import say_goodbuy 

module.say_hello()
say_goodbuy()
