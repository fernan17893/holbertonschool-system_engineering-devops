#!/usr/bin/python3
"""
Export data in a JSON file
"""

import json
import requests
import sys

if __name__ == "__main__":
    if sys.argv[1].isdigit() is True:
        user_id = int(sys.argv[1])

    user_api = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    users = json.loads(user_api.text)
    users = users['username']
    todo_api = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = json.loads(todo_api.text)
    file = sys.argv[1] + '.json'
    my_list = []
    json_str = {}
    for task in todos:
        _dic = {}
        _dic["task"] = task["title"]
        _dic["completed"] = task["completed"]
        _dic["username"] = users
        my_list.append(_dic)
        json_str[sys.argv[1]] = my_list
        with open(file, 'w') as f:
            json.dump(json_str, f)
