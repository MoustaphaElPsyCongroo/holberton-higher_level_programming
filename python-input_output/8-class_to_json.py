#!/usr/bin/python3
"Gets the dictionary description of an instance for JSON serialization"


def class_to_json(obj):
    """
    Gets the dictionary description of an instance object for JSON
    serialization
    """
    return obj.__dict__
