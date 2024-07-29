#!/usr/bin/python3
"""fetch data from API and save it on json file"""
import json
import requests
import sys


def main():
    args = sys.argv[1:]

    if args:
        id = args[0]

        todoApiUrl = 'https://jsonplaceholder.typicode.com/todos'
        userApiUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

        todoTasks = requests.get(url=todoApiUrl).json()
        userName = requests.get(url=userApiUrl).json()['username']

        tasksNumber = 0
        task_completed = 0

        data = {id: []}
        for user in todoTasks:
            if user['userId'] == int(id):
                data[id] += [{"task": user['title'],
                              "completed": user['completed'],
                              "username": userName}]

        filename = f'{id}.json'
        with open(filename, mode='w', newline='') as file:
            json.dump(data, file)


if __name__ == "__main__":
    main()
