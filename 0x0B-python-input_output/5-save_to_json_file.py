#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, 'w') as f:
        json.dump(obj, f)
