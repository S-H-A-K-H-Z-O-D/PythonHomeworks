import requests, json, csv

res = requests.get("https://jsonplaceholder.typicode.com/comments")
data = res.json()

with open("comments.json", "wt") as file:
    json.dump(data, file, indent=4)

with open("comments.json") as file:
    cont = json.load(file)

    with open("comments.csv", "wt", newline='') as f:
        headers = cont[0].keys() if cont else []
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(cont)