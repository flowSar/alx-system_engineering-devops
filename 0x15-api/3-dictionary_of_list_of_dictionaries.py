#!/usr/bin/python3
"""fetch all data for all users using API and save it on json file"""
import json
import requests
import sys


def main():

    todoApiUrl = 'https://jsonplaceholder.typicode.com/todos'
    userUrl = 'https://jsonplaceholder.typicode.com/users'
    userTasks = requests.get(url=todoApiUrl).json()
    users = requests.get(url=userUrl).json()

    tasksNumber = 0
    task_completed = 0

    data = {}

    for user in users:
        userId = user['id']

        data[userId] = []
        for task in userTasks:
            if userId == task['userId']:
                data[userId] += [{'username': user['username'],
                                  'task': task['title'],
                                  'completed': task['completed']}]

    filename = 'todo_all_employees.json'
    with open(filename, mode='w', newline='') as file:
        json.dump(data, file)


if __name__ == "__main__":
    main()
