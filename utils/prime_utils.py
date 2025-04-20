"""
Prime Number Utility Functions

This module provides additional utility functions for working with prime numbers.
"""

def prime_factors(n):
    """
    Find all prime factors of a number.
    
    Args:
        n (int): The number to factorize
        
    Returns:
        list: A list of prime factors
    """
    factors = []
    
    # Handle 2 separately
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check odd factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors

def is_mersenne_prime(p):
    """
    Check if 2^p - 1 is a Mersenne prime.
    This uses the Lucas-Lehmer test.
    
    Args:
        p (int): The exponent to check
        
    Returns:
        bool: True if 2^p - 1 is prime, False otherwise
    """
    # Check if p itself is prime (required for Mersenne prime)
    from prime_generator import is_prime
    if not is_prime(p):
        return False
    
    # Implement Lucas-Lehmer test
    s = 4
    m = (2 ** p) - 1
    
    for _ in range(p - 2):
        s = ((s * s) - 2) % m
    
    return s == 0

def twin_primes(limit):
    """
    Find all twin primes up to a limit.
    Twin primes are pairs of primes that differ by 2.
    
    Args:
        limit (int): Upper bound for the search
        
    Returns:
        list: List of tuples containing twin prime pairs
    """
    from prime_generator import generate_primes
    
    primes = generate_primes(limit)
    twins = []
    
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            twins.append((primes[i], primes[i + 1]))
    
    return twins
