"""
=============================================================================
                PRACTICE PROBLEMS - FILE I/O
=============================================================================

This file contains practice problems for File Input/Output operations.

=============================================================================
"""


# =============================================================================
# PROBLEM 1: File Operations - Write, Replace, Search
# =============================================================================
"""
Write a Python program to perform the following operations:

1. Create a new file named practice.txt and write content in it
2. Write a function to replace all occurrences of "Java" with "Python"
3. Search whether the word "learning" exists in the file
"""

print("=" * 50)
print("PROBLEM 1: File Operations")
print("=" * 50)

# Step 1: Create and write data to the file
with open("practice.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning File I/O\n")
    f.write("using Java.\n")
    f.write("I like programming in Java.\n")

print("File 'practice.txt' created with initial content.")

# Show initial content
print("\nInitial content:")
print("-" * 30)
with open("practice.txt", "r") as f:
    print(f.read())


# Step 2: Function to replace 'Java' with 'Python'
def replace_java_with_python():
    with open("practice.txt", "r") as f:
        data = f.read()

    data = data.replace("Java", "Python")

    with open("practice.txt", "w") as f:
        f.write(data)
    
    print("Replaced 'Java' with 'Python'")


# Step 3: Function to search for 'learning'
def search_learning():
    with open("practice.txt", "r") as f:
        content = f.read()
        if "learning" in content:
            print("The word 'learning' exists in the file.")
        else:
            print("The word 'learning' does not exist in the file.")


# Run the functions
replace_java_with_python()

print("\nContent after replacement:")
print("-" * 30)
with open("practice.txt", "r") as f:
    print(f.read())

search_learning()

"""
Output:
-------
The word 'learning' exists in the file.
"""


# =============================================================================
# PROBLEM 2: Find Line Number of a Word
# =============================================================================
"""
Write a Python function to find the line number where the word "learning" 
occurs first in a given file.
- Return the line number (starting from 1)
- Return -1 if the word does not exist in the file
"""

print("\n" + "=" * 50)
print("PROBLEM 2: Find Line Number of a Word")
print("=" * 50)

def find_learning_line(filename):
    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            if "learning" in line:
                return line_number
    return -1

# Example usage:
filename = "practice.txt"
result = find_learning_line(filename)
print(f"Line number where 'learning' appears: {result}")


# =============================================================================
# BONUS PROBLEMS
# =============================================================================

print("\n" + "=" * 50)
print("BONUS PROBLEM 1: Count Words in File")
print("=" * 50)

def count_words(filename):
    with open(filename, "r") as f:
        content = f.read()
        words = content.split()
        return len(words)

word_count = count_words("practice.txt")
print(f"Total words in 'practice.txt': {word_count}")


print("\n" + "=" * 50)
print("BONUS PROBLEM 2: Count Lines in File")
print("=" * 50)

def count_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        return len(lines)

line_count = count_lines("practice.txt")
print(f"Total lines in 'practice.txt': {line_count}")


print("\n" + "=" * 50)
print("BONUS PROBLEM 3: Count Occurrences of a Word")
print("=" * 50)

def count_word_occurrences(filename, word):
    with open(filename, "r") as f:
        content = f.read().lower()
        return content.count(word.lower())

count = count_word_occurrences("practice.txt", "Python")
print(f"Occurrences of 'Python' in file: {count}")


print("\n" + "=" * 50)
print("BONUS PROBLEM 4: Copy File Contents")
print("=" * 50)

def copy_file(source, destination):
    with open(source, "r") as src:
        content = src.read()
    
    with open(destination, "w") as dest:
        dest.write(content)
    
    print(f"Copied '{source}' to '{destination}'")

copy_file("practice.txt", "practice_copy.txt")

# Verify copy
print("\nContent of copied file:")
print("-" * 30)
with open("practice_copy.txt", "r") as f:
    print(f.read())


print("\n" + "=" * 50)
print("BONUS PROBLEM 5: Read Specific Lines")
print("=" * 50)

def read_specific_lines(filename, start_line, end_line):
    """Read lines from start_line to end_line (inclusive)"""
    with open(filename, "r") as f:
        lines = f.readlines()
        # Adjust for 0-based indexing
        selected = lines[start_line - 1:end_line]
        return selected

print(f"Lines 2-3 of 'practice.txt':")
for i, line in enumerate(read_specific_lines("practice.txt", 2, 3), start=2):
    print(f"  Line {i}: {line.strip()}")


print("\n" + "=" * 50)
print("BONUS PROBLEM 6: Reverse File Content")
print("=" * 50)

def reverse_file_lines(filename):
    """Reverse the order of lines in a file"""
    with open(filename, "r") as f:
        lines = f.readlines()
    
    reversed_lines = lines[::-1]
    
    with open("reversed_" + filename, "w") as f:
        f.writelines(reversed_lines)
    
    print(f"Created 'reversed_{filename}' with reversed lines")

reverse_file_lines("practice.txt")

print("\nContent of reversed file:")
print("-" * 30)
with open("reversed_practice.txt", "r") as f:
    print(f.read())


# =============================================================================
# CLEANUP
# =============================================================================

print("\n" + "=" * 50)
print("CLEANUP")
print("=" * 50)

import os

# Clean up test files
test_files = ["practice.txt", "practice_copy.txt", "reversed_practice.txt"]
for f in test_files:
    if os.path.exists(f):
        os.remove(f)
        print(f"Removed: {f}")
