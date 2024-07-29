#!/usr/bin/python3
"""fetch data from API"""
import requests
import sys


def main():
    args = sys.argv[1:]

    if args:
        id = args[0]

        todoApiUrl = 'https://jsonplaceholder.typicode.com/todos'
        userApiUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

        todoTasks = requests.get(url=todoApiUrl).json()
        EMPLOYEE_NAME = requests.get(url=userApiUrl).json()['name']

        tasksNumber = 0
        task_completed = 0
        tasks = []

        for user in todoTasks:
            if user['userId'] == int(id):
                tasksNumber += 1
                if user['completed'] is True:
                    task_completed += 1
                    tasks.append(user['title'])

        print('Employee {} is done with tasks({}/{}):'
              .format(EMPLOYEE_NAME, task_completed, tasksNumber))
        for task in tasks:
            print(f'    {task}')


if __name__ == "__main__":
    main()
