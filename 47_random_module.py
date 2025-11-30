"""
=============================================================================
                        RANDOM MODULE
=============================================================================

The random module provides functions for generating random numbers,
selecting random items, and shuffling sequences.

Key Functions:
--------------
Function                Description
--------                -----------
randint(a, b)           Random integer between a and b (inclusive)
random()                Random float between 0.0 and 1.0
uniform(a, b)           Random float between a and b
choice(seq)             Random element from a sequence
choices(seq, k)         Random k elements with replacement
sample(seq, k)          Random k elements without replacement
shuffle(list)           Shuffle list in place

=============================================================================
"""

import random

# =============================================================================
# RANDOM INTEGER - randint()
# =============================================================================
"""
randint(a, b) returns a random integer N such that a <= N <= b
Both endpoints are included!
"""

print("=" * 50)
print("RANDOM INTEGER - randint()")
print("=" * 50)

# Random integer between 1 and 10 (inclusive)
print("Random integers between 1 and 10:")
for i in range(5):
    print(f"  Roll {i+1}: {random.randint(1, 10)}")

# Dice roll simulation
print("\nDice roll simulation:")
for i in range(3):
    print(f"  Roll {i+1}: {random.randint(1, 6)}")


# =============================================================================
# RANDOM FLOAT - random() and uniform()
# =============================================================================

print("\n" + "=" * 50)
print("RANDOM FLOAT - random() and uniform()")
print("=" * 50)

# random() returns float between 0.0 and 1.0
print("random() - Float between 0.0 and 1.0:")
for i in range(3):
    print(f"  {random.random():.4f}")

# uniform(a, b) returns float between a and b
print("\nuniform(1, 5) - Float between 1.0 and 5.0:")
for i in range(3):
    print(f"  {random.uniform(1, 5):.4f}")


# =============================================================================
# RANDOM CHOICE - choice()
# =============================================================================
"""
choice(sequence) returns a random element from a non-empty sequence
(list, tuple, or string).
"""

print("\n" + "=" * 50)
print("RANDOM CHOICE - choice()")
print("=" * 50)

# Random choice from a list
colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Colors: {colors}")
print("Random colors:")
for i in range(3):
    print(f"  {random.choice(colors)}")

# Random choice from a string
letters = "ABCDEFGHIJ"
print(f"\nLetters: {letters}")
print(f"Random letter: {random.choice(letters)}")

# Random choice from a tuple
directions = ("North", "South", "East", "West")
print(f"\nDirections: {directions}")
print(f"Random direction: {random.choice(directions)}")


# =============================================================================
# SHUFFLE - shuffle()
# =============================================================================
"""
shuffle(list) shuffles the list in place (modifies the original list).
Returns None.
"""

print("\n" + "=" * 50)
print("SHUFFLE - shuffle()")
print("=" * 50)

cards = [1, 2, 3, 4, 5]
print(f"Original list: {cards}")

random.shuffle(cards)
print(f"After shuffle: {cards}")

random.shuffle(cards)
print(f"Shuffled again: {cards}")

# Shuffle a deck of cards
deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
print(f"\nOriginal deck: {deck}")
random.shuffle(deck)
print(f"Shuffled deck: {deck}")


# =============================================================================
# SAMPLE - sample()
# =============================================================================
"""
sample(sequence, k) returns k unique random elements from the sequence.
Unlike choices(), sample() doesn't repeat elements.
"""

print("\n" + "=" * 50)
print("SAMPLE - sample()")
print("=" * 50)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers: {numbers}")

# Pick 3 unique random numbers
picked = random.sample(numbers, 3)
print(f"3 random unique numbers: {picked}")

# Lottery numbers (6 from 1-49)
lottery_pool = list(range(1, 50))
lottery_numbers = sorted(random.sample(lottery_pool, 6))
print(f"\nLottery numbers (6 from 1-49): {lottery_numbers}")


# =============================================================================
# CHOICES - choices() (with replacement)
# =============================================================================
"""
choices(sequence, k=1) returns a list of k random elements with replacement.
Elements can repeat!
"""

print("\n" + "=" * 50)
print("CHOICES - choices() (with replacement)")
print("=" * 50)

colors = ["red", "green", "blue"]
print(f"Colors: {colors}")

# Pick 5 colors (can repeat)
picked_colors = random.choices(colors, k=5)
print(f"5 random colors (may repeat): {picked_colors}")

# Weighted choices
weighted_colors = random.choices(
    ["red", "green", "blue"],
    weights=[10, 1, 1],  # red is 10x more likely
    k=10
)
print(f"\nWeighted choices (red 10x likely): {weighted_colors}")


# =============================================================================
# SETTING SEED - seed()
# =============================================================================
"""
seed(n) initializes the random number generator.
Using the same seed produces the same sequence of random numbers.
Useful for reproducibility.
"""

print("\n" + "=" * 50)
print("SETTING SEED - seed()")
print("=" * 50)

# Without seed - different each time
print("Without seed (different each time):")
print(f"  {random.randint(1, 100)}, {random.randint(1, 100)}, {random.randint(1, 100)}")

# With seed - reproducible
print("\nWith seed(42) - first run:")
random.seed(42)
print(f"  {random.randint(1, 100)}, {random.randint(1, 100)}, {random.randint(1, 100)}")

print("\nWith seed(42) - second run (same results!):")
random.seed(42)
print(f"  {random.randint(1, 100)}, {random.randint(1, 100)}, {random.randint(1, 100)}")


# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# 1. Password Generator
print("\n1. Random Password Generator:")
import string
chars = string.ascii_letters + string.digits + "!@#$%"
password = ''.join(random.choices(chars, k=12))
print(f"   Generated password: {password}")

# 2. Coin Flip
print("\n2. Coin Flip Simulation (10 flips):")
flips = [random.choice(["Heads", "Tails"]) for _ in range(10)]
print(f"   Results: {flips}")
print(f"   Heads: {flips.count('Heads')}, Tails: {flips.count('Tails')}")

# 3. Random Quote
print("\n3. Random Quote Generator:")
quotes = [
    "Be the change you wish to see.",
    "Stay hungry, stay foolish.",
    "Think different.",
    "Just do it.",
    "Keep it simple."
]
print(f"   Today's quote: \"{random.choice(quotes)}\"")

# 4. Random Team Generator
print("\n4. Random Team Generator:")
players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
random.shuffle(players)
team1 = players[:3]
team2 = players[3:]
print(f"   Team 1: {team1}")
print(f"   Team 2: {team2}")
