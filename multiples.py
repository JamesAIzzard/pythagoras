from typing import List

from typing import Dict

import primes


def get_lcm(values: List[int]) -> int:
    """Returns the lowest common multiple of the list of integers provided."""
    # Find prime factors for each input value
    prime_factors: Dict[int, Dict[int, int]] = {}
    for value in values:
        prime_factors[value] = primes.find_prime_factors(value)

    # Find largest quantity of each factor
    factor_quantities:Dict[int, int] = {}
    for value in prime_factors.keys():
        for factor, exp in prime_factors[value].items():
            if factor not in factor_quantities:
                factor_quantities[factor] = exp
            else:
                if exp > factor_quantities[factor]:
                    factor_quantities[factor] = exp

    # Sum the factors * exps
    factor_product_sum = 1
    for factor, exp in factor_quantities.items():
        factor_product_sum *= (factor ** exp)
    
    return factor_product_sum
