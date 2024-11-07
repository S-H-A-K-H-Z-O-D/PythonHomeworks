import requests, json, csv

res = requests.get("https://jsonplaceholder.typicode.com/users")
data = res.json()

with open("users.json", "wt") as file:
    json.dump(data, file, indent=4)

with open("users.json") as f:
    cont = json.load(f)

    with open("users.csv", "wt", newline='') as csvF:
        headers = cont[0].keys() if cont else []
        writer = csv.DictWriter(csvF, fieldnames=headers)
        writer.writeheader()
        writer.writerows(cont)