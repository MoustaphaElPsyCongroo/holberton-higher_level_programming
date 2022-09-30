#!/usr/bin/python3
"Decodes a JSON object"
import json


def from_json_string(my_str):
    "Decodes a JSON object"
    return json.loads(my_str)
