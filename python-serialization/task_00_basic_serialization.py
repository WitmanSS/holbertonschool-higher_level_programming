#!/usr/bin/env python3
import json
"""
A module providing basic serialization and deserialization functionalities
for Python dictionaries using JSON format.
"""


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON format and saves it to a file.

    If the output file already exists, it will be replaced (overwritten).

    Args:
        data (dict): The Python dictionary containing data to be serialized.
        filename (str): The filename of the output JSON file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # Use json.dump to write the dictionary (data) to the file object (f)
            json.dump(data, f)
    except Exception as e:
        print(f"An error occurred during serialization: {e}")


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file to a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: The deserialized Python Dictionary.
              Returns an empty dictionary if the file cannot be loaded.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # Use json.load to read the JSON data from the file object (f)
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' contains invalid JSON.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred during deserialization: {e}")
        return {}
