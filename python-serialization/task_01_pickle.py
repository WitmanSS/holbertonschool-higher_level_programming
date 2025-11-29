#!/usr/bin/env python3
import pickle
import os
"""
A module defining the CustomObject class with serialization and deserialization
functionality using the pickle module.
"""


class CustomObject:
    """
    A custom class that holds object data and provides methods for
    serializing and deserializing its instances using pickle.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes in a readable format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance of the object using pickle and saves
        it to the provided filename.

        Args:
            filename (str): The filename to save the serialized object to.

        Returns:
            bool: True on success, False on failure.
        """
        try:
            # 'wb' mode for writing in binary format
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            return True
        except Exception as e:
            # Handle potential exceptions during file writing or pickling
            print(f"Serialization failed: {e}")
            return False

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and deserializes an instance of CustomObject from the provided filename
        using pickle.

        Args:
            filename (str): The filename to load the serialized object from.

        Returns:
            CustomObject or None: The deserialized instance of CustomObject,
                                  or None if the file is not found or malformed.
        """
        try:
            # 'rb' mode for reading in binary format
            with open(filename, 'rb') as f:
                # Use pickle.load to read and reconstruct the object
                return pickle.load(f)
        except FileNotFoundError:
            # Handle case where the file does not exist
            print(f"Deserialization failed: File '{filename}' not found.")
            return None
        except (pickle.UnpicklingError, EOFError):
            # Handle cases where the file contains corrupted or malformed pickle data
            print(f"Deserialization failed: Invalid or malformed pickle data in '{filename}'.")
            return None
        except Exception as e:
            # Handle any other unexpected exceptions
            print(f"Deserialization failed: An unexpected error occurred: {e}")
            return None
