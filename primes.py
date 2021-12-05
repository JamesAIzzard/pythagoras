from typing import Dict, List

def check_if_prime(value: int) -> bool:
    """Returns True/False to indicate if the value is prime or not."""
    # Avoid special case of 1 and exclude values less than 1
    if value <= 1:
        return False
    # Go ahead and run algorithm
    divisor = 2
    while divisor < value:
        dividend = value / divisor
        if dividend.is_integer():
            return False
        divisor += 1
    return True

def get_primes_smaller_than(n: int) -> List[int]:
    """Returns a list of prime numbers smaller than n."""
    i = 2
    results: List[int] = []
    while i < n:
        if check_if_prime(i) is True:
            results.append(i)
        i += 1
    return results
        

def find_prime_factors(value: int) -> Dict[int, int]:
    """Returns the prime factors of the provided integer as a dictionary structure.
    The dictionary keys represent the prime factors.
    The dictionary values represents their indices.
    For example, we would express 24 = 2^2 * 3^1 as follows:
    {
        2: 2,
        3: 1
    }
    """
    # Avoid special case of 1 and exclude values less than 1
    if value <= 1:
        return {}
    # Avoid wasting time if value is prime
    if check_if_prime(value):
        return {value: 1}

    # Go ahead and run algorithm
    results: Dict[int, int] = {}
    primes_smaller_than_value = []
    while value not in primes_smaller_than_value:
        primes_smaller_than_value = get_primes_smaller_than(value)
        for prime in primes_smaller_than_value:
            dividend = value / prime
            if dividend.is_integer():
                if prime not in results.keys():
                    results[prime] = 1
                else:
                    results[prime] += 1
                break
        value = dividend
    # if value not in results.keys():
    #     results[value] = 1
    # else:
    #     results[value] += 1
    results[value] = 1
    return results
    

    
