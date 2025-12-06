#!/usr/bin/python3
"""
A module containing a function to generate personalized invitation files
from a template and a list of attendee objects.
"""
import os
import logging

# Configure logging to output to console
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.

    Args:
        template (str): The invitation template string with placeholders.
        attendees (list): A list of dictionaries, where each dictionary
                          contains data for one attendee.
    """
    # 1. Check Input Types
    if not isinstance(template, str):
        logging.error("Invalid input: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input: Attendees must be a list of dictionaries.")
        return

    # 2. Handle Empty Template
    if not template:
        logging.error("Template is empty, no output files generated.")
        return

    # 3. Handle Empty Attendees List
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # Define the required placeholders
    placeholders = ["{name}", "{event_title}", "{event_date}", "{event_location}"]
    
    # 4. Process Each Attendee and Generate Output Files
    for index, attendee in enumerate(attendees, 1):
        processed_template = template
        output_filename = f"output_{index}.txt"
        
        # Iterate over placeholders to replace them
        for placeholder in placeholders:
            key = placeholder.strip("{}")
            
            # Retrieve value, handling missing or None values with "N/A"
            value = attendee.get(key)
            if value is None:
                replacement = "N/A"
            else:
                replacement = str(value)
            
            # Replace the placeholder in the template
            processed_template = processed_template.replace(placeholder, replacement)
        
        # 5. Write the processed template to the output file
        try:
            with open(output_filename, 'w') as f:
                f.write(processed_template)
            logging.info(f"Successfully generated invitation for {attendee.get('name', 'N/A')} in {output_filename}")
        except IOError as e:
            logging.error(f"Could not write file {output_filename}: {e}")
            
# --- Example Usage (as defined in the instructions) ---
if __name__ == '__main__':
    # Create the template file content required for the test
    template_content_str = (
        "Hello {name},\n\n"
        "You are invited to the {event_title} on {event_date} at {event_location}.\n\n"
        "We look forward to your presence.\n\n"
        "Best regards,\n"
        "Event Team\n"
    )
    
    # Write the template to a file
    try:
        with open('template.txt', 'w') as file:
            file.write(template_content_str)
    except IOError:
        logging.error("Could not create template.txt file. Cannot run example.")
        exit(1)

    # Read the template from a file
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # List of attendees
    attendees_data = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"} # Test case for missing data (event_date=None)
    ]

    # Test Case 1: Standard execution
    print("\n--- Test Case 1: Standard Execution ---")
    generate_invitations(template_content, attendees_data)

    # Test Case 2: Empty template
    print("\n--- Test Case 2: Empty Template ---")
    generate_invitations("", attendees_data)

    # Test Case 3: Empty attendees list
    print("\n--- Test Case 3: Empty Attendees List ---")
    generate_invitations(template_content, [])
    
    # Test Case 4: Invalid input types (Template not string)
    print("\n--- Test Case 4: Invalid Template Type ---")
    generate_invitations(123, attendees_data)
    
    # Test Case 5: Invalid input types (Attendees not list of dicts)
    print("\n--- Test Case 5: Invalid Attendees Type ---")
    generate_invitations(template_content, "not_a_list")
    
    # Test Case 6: Invalid input types (List contains non-dict)
    print("\n--- Test Case 6: Invalid List Content ---")
    generate_invitations(template_content, attendees_data + ["not_a_dict"])
