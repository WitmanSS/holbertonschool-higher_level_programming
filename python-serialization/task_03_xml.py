#!/usr/bin/env python3
import xml.etree.ElementTree as ET
"""
A module providing functions for serializing Python dictionaries to XML 
and deserializing XML back into dictionaries.
"""


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML format and saves it to a file.

    The root element is <data>, and each key-value pair becomes a child element.

    Args:
        dictionary (dict): The Python dictionary to serialize.
        filename (str): The filename of the output XML file.
    """
    try:
        # Create the root element
        root = ET.Element("data")

        # Iterate through dictionary items and create child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            # Convert all values to string format for storage in XML
            child.text = str(value)

        # Create an ElementTree wrapper and write it to the file
        tree = ET.ElementTree(root)
        
        # Use short_empty_elements=False to ensure elements without attributes 
        # (like <name>John</name>) are written properly.
        # Use encoding="utf-8" and xml_declaration=True for standard XML file.
        tree.write(filename, encoding='utf-8', xml_declaration=True)

    except Exception as e:
        print(f"An error occurred during XML serialization: {e}")


def deserialize_from_xml(filename):
    """
    Reads XML data from a file and reconstructs a Python dictionary.

    Args:
        filename (str): The filename of the input XML file.

    Returns:
        dict or None: The deserialized Python dictionary, or None if an error occurs.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        deserialized_data = {}

        # Iterate through child elements of the root (which should be <data>)
        for child in root:
            # The tag is the key, and the text is the value
            # Since the original data was stored as strings, we read it back as strings
            deserialized_data[child.tag] = child.text

        return deserialized_data

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except ET.ParseError:
        print(f"Error: The file '{filename}' contains malformed XML.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during XML deserialization: {e}")
        return None
