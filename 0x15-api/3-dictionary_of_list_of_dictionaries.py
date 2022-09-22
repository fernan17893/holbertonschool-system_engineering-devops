#!/usr/bin/python3
"""Return API todo list dictionary """

import csv
import json
import requests
import sys

if __name__ == "__main__":

    """Fetch users"""
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/')
    users = json.loads(user.text)

    """Fetch the todo tasks"""
    response = requests.get(
        'https://jsonplaceholder.typicode.com/todos/')
    tasks_list = json.loads(response.text)

    """create json file"""
    with open('todo_all_employees.json', 'w', encoding='utf-8') as jsonfile:
        u_info = {}
        for user in users:
            forma = []
            j_myson = {}
            for tasks in tasks_list:
                if user['id'] == tasks['userId']:
                    j_myson['username'] = user['username']
                    j_myson['task'] = tasks['title']
                    j_myson["completed"] = tasks['completed']
                    copy = j_myson.copy()
                    forma.append(copy)
            u_info[user['id']] = forma
        json.dump(u_info, jsonfile)
