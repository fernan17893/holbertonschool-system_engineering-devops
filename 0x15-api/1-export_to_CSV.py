#!/usr/bin/python3
"""
Export data in a CSV file
"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    if sys.argv[1].isdigit() is True:
        user_id = int(sys.argv[1])

    user_api = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    users = json.loads(user_api.text)
    todo_api = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = json.loads(todo_api.text)
    _file = sys.argv[1] + ".csv"
    with open(_file, 'w') as f:
        _write = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in todos:
            _write.writerow(
                [sys.argv[1],
                    users['username'],
                    task['completed'],
                    task['title']])
