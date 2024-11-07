import requests, json, csv, os

res = requests.get("https://jsonplaceholder.typicode.com/photos")
data = res.json()

with open('photos.json', "wt") as file:
    json.dump(data, file, indent=4)

with open('photos.json') as file:
    cont = json.load(file)
    os.makedirs("images", exist_ok=True)

    with open('photos.csv', 'wt', newline='') as f:
        headers = cont[0].keys() if cont else []
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(cont)

    for el in cont:
        img = requests.get(el['url'])
        img_name = f"images/img{el["id"]}.png"

        with open(img_name, 'wb') as file:
            file.write(img.content)