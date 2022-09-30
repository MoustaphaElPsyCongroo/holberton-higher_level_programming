#!/usr/bin/python3
"""Saves all arguments of this script to a file"""


from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = argv[1:]

previous_cnts = load_from_json_file('add_item.json')
tosav = [*previous_cnts, *args]
save_to_json_file(tosav, "add_item.json")
