
import re


def count_pattern_occurrences_in_file(file_path):
    """
    Finds all occurrences of a pattern that starts with 'un', has unlimited letters, and ends with 'an' in a text file.

    Args:
        text.txt (str): The path to the text file to search within.

    Returns:
        int: The number of matches found in the file.
    """
    try:
        # Open and read the file
        with open("text.txt", 'r') as f:
           text = "text.txt"

        # Define the pattern: "un", followed by any number of letters, ending with "an"
        pattern = r'\bun[a-zA-Z]*an\b'

        # Find all matches using re.findall
        matches = re.findall(pattern, text)

        # Return the count of matches
        return len(matches)

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return 0