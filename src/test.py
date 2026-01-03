import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from itertools import product
from temp import Arithmatique as arith

low_bound = -10
hi_bound = 21


def is_trivial(pair: tuple[int, int]) -> bool:
    trivial_cases = (-1, 0, 1)
    return any(n in trivial_cases for n in pair)

def is_integer(num: int) -> bool:
    return num % 1 == 0

def get_density_distribution(data):

    data_range = np.arange(len(data))
    pdf = norm.pdf(data_range, loc=0, scale=50)
    p = pdf / pdf.sum()

    return p
    
def get_expr():

    # Prep dataset
    r = np.arange(low_bound, hi_bound + 1)
    x = np.arange(low_bound + 1)


    r = np.random.choice(r, p=get_density_distribution(r))
    x = np.random.choice(x, p=get_density_distribution(x))
    y = r - x

    return f"{x} + {y} = {r}"

for _ in range(10):
    print(get_expr())



# all_pairs = np.array([pair for pair in product(x, y) if not is_trivial(pair)])

# # Create subsets for each operation type
# add_data = np.array([(x, y) for x, y in all_pairs if low_bound <= x + y <= hi_bound])
# sub_data = np.array([(x, y) for x, y in all_pairs if low_bound <= x - y <= hi_bound])
# mul_data = np.array([(x, y) for x, y in all_pairs if low_bound <= x * y <= hi_bound])
# div_data = np.array([(x, y) for x, y in all_pairs if low_bound <= x/y <= hi_bound and is_integer(x/y)])

# # Apply distribution for random choice
# data = np.array([data[np.random.choice(data_range, p=p)] for _ in range(10)])

# # Retrieve results
# print(data)
# result = data[:, 0] * data[:, 1]
# print(result)
# print(np.mean(result))


# Je veux pouvoir controler le range des resultats, mais comment
# je peux m'assurer que les nombres 

# Denombrement de toutes les facons d'obtenir chaque resultat dans l'intervalle?

# Contre-exemple :
# low_bound = 10000
# hi_bound = 10100

