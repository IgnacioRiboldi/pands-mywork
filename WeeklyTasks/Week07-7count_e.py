# E counter
# This program takes one txt file and counts how many 'E' contains
# By Ignacio Riboldi

import sys
import os

def count_e_in_file(filename):
    """Counts the number of 'e' characters in a given text file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            e_count = content.lower().count('e')
            return e_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except IsADirectoryError:
        print(f"Error: The path '{filename}' is a directory, not a file.")
        return None
    except IOError:
        print(f"Error: An error occurred while reading the file '{filename}'.")
        return None

def main():
    """Main function that takes a command-line argument (filename) and counts 'e' characters."""
    if len(sys.argv) != 2:
        print("Usage: python count_e.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    # Check if the file exists and is a regular file (not a directory)
    if not os.path.isfile(filename):
        print(f"Error: '{filename}' is not a valid file.")
        sys.exit(1)

    e_count = count_e_in_file(filename)
    
    if e_count is not None:
        print(f"The number of 'e' characters in '{filename}' is: {e_count}")

if __name__ == "__main__":
    main()
