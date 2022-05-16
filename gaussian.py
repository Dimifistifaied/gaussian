from math import sqrt, exp, pow, e, pi
import numpy as np
x = np.random.rand(1, 100000)
y = []
for i in x[0]:
    new_prob = (1 / (np.std(x) * sqrt(2 * pi))) * pow(e, (
                    -(pow(i - np.mean(x), 2))/pow(2*np.std(x), 2)))
    y.append(new_prob)

    print(y)
    pyplot.plot(x[0], y)
    pyplot.show()
