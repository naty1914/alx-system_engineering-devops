#!/usr/bin/python3
"""A  script that export all employees data to JSON format"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(url + "users").json()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user.get("id"): [{
                "task": td.get("title"),
                "completed": td.get("completed"),
                "username": user.get("username")
            } for td in requests.get(url + "todos",
                                     params={"userId": user.get("id")}).json()]
            for user in user_response}, jsonfile)
