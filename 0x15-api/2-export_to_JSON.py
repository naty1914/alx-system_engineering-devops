#!/usr/bin/python3
"""A  script that export data to JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(id)).json()
    todos_resp = requests.get(url + "todos", params={"userId": id}).json()

    todos_completed = [todo.get("title") for todo
                       in todos_resp if todo.get("completed") is True]
    username = user_response.get("username")
    with open("{}.json".format(id), "w") as jsonfile:
        json.dump({id: [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            } for todo in todos_resp]}, jsonfile)
