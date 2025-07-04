#!/usr/bin/python3

"""
This module fetches data from the JsonPlaceholder REST API given an employee ID, and displays
info about his/her TODO list progress.
"""

import sys
import requests

employee_id = int(sys.argv[1])
num_completed_todos = 0

response_todos = requests.get("https://jsonplaceholder.typicode.com/todos")
response_users = requests.get("https://jsonplaceholder.typicode.com/users")

def get_employee_name(users, id):
    for user in users:
        if user["id"] == id:
            return user["name"]

def get_num_of_completed_tasks(tasks, id):
    num_tasks = 0
    for task in tasks:
        if task["userId"] == id and task["completed"] == True:
            num_tasks = num_tasks + 1
    return num_tasks

def get_num_of_tasks(tasks, id):
    num_tasks = 0
    for task in tasks:
        if task["userId"] == id:
            num_tasks = num_tasks + 1
    return num_tasks

def main():
    if response_todos.status_code == 200 and response_users.status_code == 200:
        todos = response_todos.json()
        users = response_users.json()
        employee_name = get_employee_name(users, employee_id)
        completed_tasks = get_num_of_completed_tasks(todos, employee_id)
        completed_tasks_list = [task for task in todos if task["completed"] and task["userId"] == employee_id]
        total_tasks = get_num_of_tasks(todos, employee_id)
        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
        for task in completed_tasks_list:
            print(f"\t {task.get('title')}")

if __name__ == "__main__":
    main()