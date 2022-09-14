#!/usr/bin/python3
"""
Returns API information
"""

import json
import requests
import sys


if __name__ == "__main__":
    """ Check first arg as user ID to return information """
    if sys.argv[1].isdigit() is True:
        user_id = int(sys.argv[1])

    user_api = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    users = json.loads(user_api.text)
    todo_api = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = json.loads(todo_api.text)
    total_tasks = 0
    tasks_done = 0

    for task in todos:
        if task["userId"] == users["id"]:
            total_tasks += 1
            if task['completed']:
                tasks_done += 1
    print('Employee {} is done with tasks ({}/{}):'
          .format(users['name'], tasks_done, total_tasks))

    for task in todos:
        if task['completed']:
            print('\t {}'.format(task['title']))
