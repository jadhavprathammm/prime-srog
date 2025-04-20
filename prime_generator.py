#!/usr/bin/env python3
"""
Prime Number Generator Module

This module provides functions for generating prime numbers and testing primality.
"""

def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def generate_primes(limit):
    """
    Generate a list of prime numbers up to the specified limit.
    
    Args:
        limit (int): Upper bound for prime generation
        
    Returns:
        list: A list of prime numbers up to the limit
    """
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def nth_prime(n):
    """
    Find the nth prime number.
    
    Args:
        n (int): The position of the prime to find
        
    Returns:
        int: The nth prime number
    """
    if n <= 0:
        raise ValueError("Position must be a positive integer")
    
    count = 0
    num = 1
    
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    
    return num

if __name__ == "__main__":
    # Example usage
    print("First 10 prime numbers:")
    print(generate_primes(30))
    
    print("\nThe 10th prime number is:", nth_prime(10))
