import requests
import json
import csv

r = requests.get('https://jsonplaceholder.typicode.com/posts')
data = r.json()

with open("posts.json", "wt") as file:
    json.dump(data, file, indent=4)
    
with open("posts.json", "r") as file:
    cont = json.load(file)

    with open("posts.csv", "wt", newline='') as CSVfile:
        headers = cont[0].keys() if cont else []
        writer = csv.DictWriter(CSVfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(cont)