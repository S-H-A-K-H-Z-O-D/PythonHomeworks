import requests, json, csv

res = requests.get("https://jsonplaceholder.typicode.com/todos")
data = res.json()

with open("todos.json", "wt") as file:
    json.dump(data, file, indent=4)

with open("todos.json") as f:
    cont = json.load(f)

    with open("todos.csv", "wt", newline='') as csvF:
        headers = cont[0].keys() if cont else []
        writer = csv.DictWriter(csvF, fieldnames=headers)
        writer.writeheader()
        writer.writerows(cont)