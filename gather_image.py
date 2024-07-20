import requests
from create_character_table import get_table

URL = "https://raw.githubusercontent.com/Aceship/Arknight-Images/main/avatars"

table = get_table()

print("Running...")

for obj, details in table.items():
    target = URL + "/" + obj + ".png"
    with open(f"./img/avatars/{obj+'.png'}", "wb") as f:
        f.write(requests.get(target).content)

print("Finished!")