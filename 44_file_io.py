"""
=============================================================================
                        FILE I/O (Input/Output)
=============================================================================

What is File I/O?
-----------------
File I/O lets your Python program read from or write to files.

File Modes:
-----------
Mode    Description
----    -----------
'r'     Read (default)
'w'     Write (overwrite)
'a'     Append
'x'     Create (fails if file exists)
'b'     Binary mode
't'     Text mode (default)
'r+'    Read and write

Common Methods:
---------------
Method          Description
------          -----------
read()          Reads entire content
readline()      Reads a single line
readlines()     Returns list of lines
write(text)     Writes string to file
writelines(list) Writes list of strings to file
close()         Closes the file

Best Practice: Use 'with' statement - automatically closes the file!

=============================================================================
"""


# =============================================================================
# WRITING TO A FILE
# =============================================================================
"""
Writing a File:
- Overwrites the file if it exists
- Creates a new file if it doesn't
- \n adds a new line
- Using 'with' is safer as it auto-closes the file
"""

print("=" * 50)
print("WRITING TO A FILE")
print("=" * 50)

# Method 1: Using 'w' mode (Write)
with open("example.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

print("File 'example.txt' created and written successfully!")


# Writing multiple lines at once using writelines()
lines = [
    "Line 1: Hello World\n",
    "Line 2: Python is awesome\n",
    "Line 3: File I/O is easy\n"
]

with open("example2.txt", "w") as file:
    file.writelines(lines)

print("File 'example2.txt' created with writelines()!")


# =============================================================================
# READING A FILE
# =============================================================================
"""
Reading a File:
- File must exist, or you'll get FileNotFoundError
- Always close the file using file.close() unless you use 'with'
"""

print("\n" + "=" * 50)
print("READING A FILE")
print("=" * 50)

# Method 1: Using open() and read() - reads entire file
print("Method 1: read() - entire file as string")
print("-" * 40)
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


# Method 2: readline() - reads one line at a time
print("Method 2: readline() - one line at a time")
print("-" * 40)
with open("example.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"Line 1: {line1.strip()}")
    print(f"Line 2: {line2.strip()}")


# Method 3: readlines() - returns list of all lines
print("\nMethod 3: readlines() - list of lines")
print("-" * 40)
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(f"Type: {type(lines)}")
    print(f"Lines: {lines}")


# Method 4: Loop through file line by line
print("\nMethod 4: Loop through file")
print("-" * 40)
with open("example.txt", "r") as file:
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.strip()}")


# =============================================================================
# APPENDING TO A FILE
# =============================================================================
"""
Appending:
- Adds content to the end of the file
- Does not overwrite existing content
- Creates file if it doesn't exist
"""

print("\n" + "=" * 50)
print("APPENDING TO A FILE")
print("=" * 50)

with open("example.txt", "a") as file:
    file.write("This line was appended.\n")
    file.write("Another appended line.\n")

print("Content appended to 'example.txt'!")

# Read to verify
print("\nFile content after appending:")
print("-" * 40)
with open("example.txt", "r") as file:
    print(file.read())


# =============================================================================
# READING AND WRITING ('r+' mode)
# =============================================================================

print("=" * 50)
print("READ AND WRITE MODE (r+)")
print("=" * 50)

# Create a test file first
with open("test_rw.txt", "w") as f:
    f.write("Original content\n")

# Read and write
with open("test_rw.txt", "r+") as file:
    content = file.read()
    print(f"Original: {content.strip()}")
    file.write("Added via r+ mode\n")

# Read to verify
with open("test_rw.txt", "r") as file:
    print(f"After r+ mode:\n{file.read()}")


# =============================================================================
# WITHOUT 'with' STATEMENT
# =============================================================================
"""
If you don't use 'with', you must manually close the file.
"""

print("=" * 50)
print("WITHOUT 'with' STATEMENT")
print("=" * 50)

file = open("example.txt", "r")
content = file.read()
print("First 50 characters:", content[:50])
file.close()  # IMPORTANT: Must close manually!
print("File closed successfully.")


# =============================================================================
# CHECKING IF FILE EXISTS
# =============================================================================

print("\n" + "=" * 50)
print("CHECKING IF FILE EXISTS")
print("=" * 50)

import os

filename = "example.txt"
if os.path.exists(filename):
    print(f"'{filename}' exists!")
    print(f"File size: {os.path.getsize(filename)} bytes")
else:
    print(f"'{filename}' does not exist.")

# Check for non-existent file
if os.path.exists("nonexistent.txt"):
    print("File exists")
else:
    print("'nonexistent.txt' does not exist.")


# =============================================================================
# DELETING A FILE
# =============================================================================
"""
To delete a file, use the os module.
Best Practice: Check if file exists first to avoid FileNotFoundError.
"""

print("\n" + "=" * 50)
print("DELETING A FILE")
print("=" * 50)

import os

# Create a file to delete
with open("to_delete.txt", "w") as f:
    f.write("This file will be deleted.")

print("File 'to_delete.txt' created.")

# Delete with safety check
if os.path.exists("to_delete.txt"):
    os.remove("to_delete.txt")
    print("File 'to_delete.txt' deleted successfully.")
else:
    print("File does not exist.")


# =============================================================================
# WORKING WITH FILE PATHS
# =============================================================================

print("\n" + "=" * 50)
print("WORKING WITH FILE PATHS")
print("=" * 50)

import os

# Get current working directory
print(f"Current directory: {os.getcwd()}")

# Join paths safely
folder = "data"
filename = "myfile.txt"
full_path = os.path.join(folder, filename)
print(f"Joined path: {full_path}")

# Get file extension
print(f"Extension of 'example.txt': {os.path.splitext('example.txt')[1]}")

# Get filename from path
print(f"Filename from path: {os.path.basename('/home/user/documents/file.txt')}")


# =============================================================================
# CLEANUP - Remove test files
# =============================================================================

print("\n" + "=" * 50)
print("CLEANUP")
print("=" * 50)

# Clean up test files created during this demo
test_files = ["example.txt", "example2.txt", "test_rw.txt"]
for f in test_files:
    if os.path.exists(f):
        os.remove(f)
        print(f"Removed: {f}")
