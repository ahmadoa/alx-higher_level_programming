#!/usr/bin/python3
"""7-add_item module"""
import sys
import json
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
jsonl = []

if os.path.exists(file):
    jsonl = load_from_json_file(file)

for i in range(1, len(sys.argv)):
    jsonl.append(sys.argv[i])

save_to_json_file(jsonl, file)
