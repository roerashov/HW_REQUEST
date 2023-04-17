import requests

class superhero:
    def __init__(self, name, intelligence):
        self.name = name
        self.intelligence = intelligence


url = 'https://akabab.github.io/superhero-api/api/all.json'
names = ['Hulk','Captain America','Thanos']
Superhero_list = []

res = requests.get(url)

for item in res.json():
    if item['name'] in names:
        Superhero_list.append(superhero(item['name'], item['powerstats']['intelligence']))

print(f' Самый умный {sorted(Superhero_list, reverse=True, key=lambda x: x.intelligence)[0].name}')

