"""
=============================================================================
                        BREAK, CONTINUE & PASS
=============================================================================

These statements are used to control the flow inside loops.

1. break    - Stops the loop immediately
2. continue - Skips the current iteration and moves to the next
3. pass     - Does nothing (placeholder)

=============================================================================
"""


# =============================================================================
# 1. break STATEMENT
# =============================================================================
"""
The break statement is used to exit (stop) a loop immediately,
even if the loop condition is still True.

Use case: Stop searching when you find what you need.
"""

print("=" * 50)
print("1. break STATEMENT")
print("=" * 50)

print("--- break example ---")
for i in range(5):
    if i == 3:
        break       # Stop the loop when i is 3
    print(i)

# Output: 0 1 2 (loop stops at 3)

print("\n--- break in while loop ---")
count = 0
while True:         # Infinite loop
    print(count)
    count += 1
    if count == 5:
        break       # Exit when count reaches 5

# Output: 0 1 2 3 4

print("\n--- Finding a number ---")
numbers = [10, 25, 30, 45, 50]
target = 30

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
    print(f"Checking {num}...")


# =============================================================================
# 2. continue STATEMENT
# =============================================================================
"""
The continue statement skips the current iteration 
and moves to the next iteration of the loop.

Use case: Skip certain values but continue the loop.
"""

print("\n" + "=" * 50)
print("2. continue STATEMENT")
print("=" * 50)

print("--- continue example ---")
for i in range(5):
    if i == 3:
        continue    # Skip when i is 3
    print(i)

# Output: 0 1 2 4 (3 is skipped)

print("\n--- Skip even numbers ---")
for i in range(1, 11):
    if i % 2 == 0:
        continue    # Skip even numbers
    print(i, end=" ")
print()

# Output: 1 3 5 7 9

print("\n--- Skip negative numbers ---")
numbers = [5, -2, 10, -7, 3, -1, 8]
print("Positive numbers only:")
for num in numbers:
    if num < 0:
        continue
    print(num, end=" ")
print()


# =============================================================================
# 3. pass STATEMENT
# =============================================================================
"""
The pass statement is a placeholder used when a statement is required 
syntactically, but no code needs to run.

Use Cases:
- Empty function or class definitions
- Placeholder for future code
- Avoid syntax errors when a block is needed
"""

print("\n" + "=" * 50)
print("3. pass STATEMENT")
print("=" * 50)

# pass in if statement
print("--- pass in if statement ---")
x = 10
if x > 5:
    pass    # Placeholder - do nothing for now
print("Program continues...")

# pass in loop
print("\n--- pass in loop ---")
for i in range(5):
    if i == 3:
        pass    # Placeholder, does nothing
    print(i)

# Output: 0 1 2 3 4 (all numbers printed, pass does nothing)

# pass in function definition
print("\n--- pass in function ---")
def future_function():
    pass    # TODO: implement later

print("Function defined but empty (no error!)")

# pass in class definition
class MyClass:
    pass    # TODO: add attributes and methods later

print("Class defined but empty (no error!)")


# =============================================================================
# COMPARISON: break vs continue vs pass
# =============================================================================

print("\n" + "=" * 50)
print("COMPARISON: break vs continue vs pass")
print("=" * 50)

print("\n--- break: stops at 3 ---")
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
print()
# Output: 0 1 2

print("\n--- continue: skips 3 ---")
for i in range(5):
    if i == 3:
        continue
    print(i, end=" ")
print()
# Output: 0 1 2 4

print("\n--- pass: does nothing at 3 ---")
for i in range(5):
    if i == 3:
        pass
    print(i, end=" ")
print()
# Output: 0 1 2 3 4
