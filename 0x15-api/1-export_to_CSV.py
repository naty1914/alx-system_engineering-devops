#!/usr/bin/python3
"""A  script that export data to CSV"""
import csv
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
    with open("{}.csv".format(id), "w", newline="") as csvfile:
        csv_write = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [csv_write.writerow(
            [id, username, todo.get("completed"), todo.get("title")]
         ) for todo in todos_resp]
