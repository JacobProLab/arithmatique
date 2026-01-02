import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from itertools import product

low_bound = -1000
hi_bound = 1000


def is_trivial(pair: tuple[int, int]) -> bool:
    trivial_cases = (0, 1)
    return any(n in trivial_cases for n in pair)

x = np.array([x for x in range(low_bound, hi_bound +1)])
y = np.array([y for y in range(low_bound, hi_bound +1)])
all_pairs = np.array([pair for pair in product(x, y) if not is_trivial(pair)])

pdf = norm.pdf(y, loc=0, scale=100)
p = pdf / pdf.sum()


data = np.array([np.random.choice(y, p=p) for _ in range(100000)])

# Histogram
plt.figure()
plt.hist(data, bins=np.arange(data.min(), data.max() + 2), align='left')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Values")
plt.show()


