#!/usr/bin/python3
"""A  script that returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(id)).json()
    todos_resp = requests.get(url + "todos", params={"userId": id}).json()

    todos_completed = [todo.get("title") for todo
                       in todos_resp if todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
          user_response.get("name"), len(todos_completed), len(todos_resp)))
    [print("\t {}".format(completed)) for completed in todos_completed]
