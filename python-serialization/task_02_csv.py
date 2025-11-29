#!/usr/bin/env python3
import csv
import json
"""
A module containing a function to convert data from a CSV file 
to a JSON file format.
"""


def convert_csv_to_json(csv_filename):
    """
    Converts data from a CSV file into a JSON file ('data.json').

    Reads the CSV data, converts each row to a dictionary, and serializes
    the resulting list of dictionaries to JSON.

    Args:
        csv_filename (str): The name of the input CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    data_list = []

    try:
        # Open the CSV file for reading
        with open(csv_filename, mode='r', encoding='utf-8') as csvfile:
            # Use DictReader to read data as a list of dictionaries
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append(row)

    except FileNotFoundError:
        # Handle the exception if the specified CSV file doesn't exist
        print(f"Error: The file '{csv_filename}' was not found.")
        return False
    except Exception as e:
        # Handle other potential reading errors
        print(f"An error occurred while reading the CSV file: {e}")
        return False

    # Proceed to serialization and writing to data.json
    try:
        # Open the output JSON file for writing
        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
            # Serialize the list of dictionaries to JSON
            json.dump(data_list, jsonfile, indent=4) # Use indent for readability
        
        return True

    except Exception as e:
        # Handle potential writing or serialization errors
        print(f"An error occurred while writing the JSON file: {e}")
        return False
