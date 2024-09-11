# In pyhton, The import statement is used to bring modules or specific 
# attributes / function / classes from module into my current working environment, 
# allowing me to access their functionality. Module are essentially python files containing
# definiations and statements, by using 'import'

import math
resutl = math.sqrt(25)       # 5

from math import sqrt, pi      # pi= 3.1416
result = sqrt(9) * pi   

from math import pi, sqrt as s
result = s(36) * pi

import math 
print(dir(math))

from importtest17 import wellcome
wellcome()
