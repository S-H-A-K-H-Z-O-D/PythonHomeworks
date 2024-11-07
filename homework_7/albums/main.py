import requests, json, csv

res = requests.get('https://jsonplaceholder.typicode.com/albums')
data = res.json()

with open("albums.json", "wt") as file:
    json.dump(data, file, indent=4)

with open("albums.json") as f:
    JsData = json.load(f)

    with open("albums.csv", "wt", newline='') as csvF:
        headers = JsData[0].keys() if JsData else []
        writer = csv.DictWriter(csvF, fieldnames=headers)
        writer.writeheader()
        writer.writerows(JsData)