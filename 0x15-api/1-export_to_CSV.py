#!/usr/bin/python3
"""fetch data from API and save it on csv file"""
import csv
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

        data = []
        for user in todoTasks:
            if user['userId'] == int(id):
                data.append([user['userId'],
                             userName,
                             user['completed'],
                             user['title']])

        filename = f'{id}.csv'
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerows(data)


if __name__ == "__main__":
    main()
