import json

# "ł" will cause the print() function to throw error as the console can not handle utf-8 encoding
def get_table():
    with open("character_table.json", "r", encoding="utf-8") as f:
        table = json.load(f)

    whitelist = ["TIER_3", "TIER_4", "TIER_5", "TIER_6"]

    characters_dict = {}
    for obj, details in table.items():
        if details["rarity"] in whitelist and details["profession"] != "TOKEN":
            characters_dict.setdefault(obj, {})

            characters_dict[obj]["name"] = details["name"]
            characters_dict[obj]["rarity"] = details["rarity"]

    return characters_dict


with open("char_lookup_table.json", "w") as f:
    json.dump(get_table(), f)