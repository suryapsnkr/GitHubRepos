import requests
import os
import json

#token = os.environ.get("GITHUB_TOKEN")

token = "YOUR_TOCKEN"

reponame = input("Please enter the repo name you want to delete : ")

GITHUB_API_URL = "https://api.github.com/"

headers = {"Authorization": "token {}".format(token)}


username = input("Please enter your GitHub username: ")

r = requests.delete("https://api.github.com/repos/{}/{}".format(username, reponame), headers=headers)

print(r)