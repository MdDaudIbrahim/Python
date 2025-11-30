"""
=============================================================================
                              RECURSION
=============================================================================

What is Recursion?
------------------
Recursion is a method of solving problems where a function calls itself.
It breaks down a complex problem into smaller, simpler subproblems.

Structure of Recursive Function:
    def function_name():
        if base_condition:
            return result          # Base case - stops recursion
        else:
            return function_name() # Recursive call

Key Points:
- Every recursive function MUST have a base case to stop the recursion
- Without a base case, it leads to infinite recursion (and crash with error)
- Useful for problems like:
    * Factorial
    * Fibonacci
    * Tree traversal
    * Tower of Hanoi

=============================================================================
"""


# =============================================================================
# FACTORIAL USING RECURSION
# =============================================================================
"""
Factorial of n (n!) = n × (n-1) × (n-2) × ... × 1

Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

Recursive approach:
    factorial(5) = 5 * factorial(4)
    factorial(4) = 4 * factorial(3)
    factorial(3) = 3 * factorial(2)
    factorial(2) = 2 * factorial(1)
    factorial(1) = 1  ← Base case
"""

print("=" * 50)
print("FACTORIAL USING RECURSION")
print("=" * 50)

def factorial(n):
    if n == 0 or n == 1:
        return 1                    # Base case
    else:
        return n * factorial(n - 1) # Recursive case

print(f"factorial(5) = {factorial(5)}")   # 120
print(f"factorial(0) = {factorial(0)}")   # 1
print(f"factorial(1) = {factorial(1)}")   # 1
print(f"factorial(7) = {factorial(7)}")   # 5040


# =============================================================================
# FIBONACCI USING RECURSION
# =============================================================================
"""
Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
Each number is the sum of the two preceding ones.

fib(n) = fib(n-1) + fib(n-2)
Base cases: fib(0) = 0, fib(1) = 1
"""

print("\n" + "=" * 50)
print("FIBONACCI USING RECURSION")
print("=" * 50)

def fibonacci(n):
    if n == 0:
        return 0                            # Base case 1
    elif n == 1:
        return 1                            # Base case 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

print("Fibonacci sequence (first 10 terms):")
for i in range(10):
    print(f"  fib({i}) = {fibonacci(i)}")


# =============================================================================
# SUM OF NATURAL NUMBERS USING RECURSION
# =============================================================================
"""
Sum of first n natural numbers = 1 + 2 + 3 + ... + n

sum(5) = 5 + sum(4)
sum(4) = 4 + sum(3)
sum(3) = 3 + sum(2)
sum(2) = 2 + sum(1)
sum(1) = 1  ← Base case
"""

print("\n" + "=" * 50)
print("SUM OF NATURAL NUMBERS")
print("=" * 50)

def sum_natural(n):
    if n == 1:
        return 1                        # Base case
    else:
        return n + sum_natural(n - 1)   # Recursive case

print(f"sum_natural(5) = {sum_natural(5)}")    # 15 (1+2+3+4+5)
print(f"sum_natural(10) = {sum_natural(10)}")  # 55


# =============================================================================
# POWER USING RECURSION
# =============================================================================
"""
Calculate x^n (x raised to power n)

power(2, 5) = 2 * power(2, 4)
power(2, 4) = 2 * power(2, 3)
...
power(2, 0) = 1  ← Base case
"""

print("\n" + "=" * 50)
print("POWER USING RECURSION")
print("=" * 50)

def power(base, exp):
    if exp == 0:
        return 1                        # Base case: x^0 = 1
    else:
        return base * power(base, exp - 1)

print(f"power(2, 5) = {power(2, 5)}")    # 32
print(f"power(3, 4) = {power(3, 4)}")    # 81
print(f"power(5, 0) = {power(5, 0)}")    # 1


# =============================================================================
# COUNTDOWN USING RECURSION
# =============================================================================

print("\n" + "=" * 50)
print("COUNTDOWN USING RECURSION")
print("=" * 50)

def countdown(n):
    if n <= 0:
        print("Liftoff!")               # Base case
    else:
        print(n)
        countdown(n - 1)                # Recursive call

countdown(5)


# =============================================================================
# REVERSE STRING USING RECURSION
# =============================================================================

print("\n" + "=" * 50)
print("REVERSE STRING USING RECURSION")
print("=" * 50)

def reverse_string(s):
    if len(s) == 0:
        return ""                       # Base case
    else:
        return s[-1] + reverse_string(s[:-1])

text = "Python"
print(f"Original: {text}")
print(f"Reversed: {reverse_string(text)}")


# =============================================================================
# RECURSION VS ITERATION
# =============================================================================

print("\n" + "=" * 50)
print("RECURSION VS ITERATION")
print("=" * 50)

# Factorial - Iterative version
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Factorial - Recursive version
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

n = 5
print(f"Iterative factorial({n}) = {factorial_iterative(n)}")
print(f"Recursive factorial({n}) = {factorial_recursive(n)}")

print("\nComparison:")
print("  Recursion: Elegant, easier to understand for some problems")
print("  Iteration: Generally more efficient (less memory overhead)")
