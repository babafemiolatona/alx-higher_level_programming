#!/usr/bin/python3
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv[1:]

# Load the existing data from the JSON file if it exists
try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    data = []

# Add the new arguments to the data list
data.extend(arguments)

# Save the updated data to the JSON file
save_to_json_file(data, "add_item.json")
