
import sys
import random as r

print(sys.path)
if '/Users/caihongxu/PycharmProjects/python-intro'  in sys.path:
    print('Yes')
else:
    sys.path.append('/Users/caihongxu/PycharmProjects/python-intro')
import prime

while True:
    hit=r.randrange(100,1000)
    print(hit)
    if hit>500:
        break

import prime


