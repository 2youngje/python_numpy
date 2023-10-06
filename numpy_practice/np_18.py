#-1 in np.reshape

import numpy as np
a = np.arange(12)

b = a.reshape((2,-1))
c = a.reshape((3,-1))
d = a.reshape((4,-1))
e = a.reshape((6,-1))

print(b.shape, c.shape, d.shape, e.shape)