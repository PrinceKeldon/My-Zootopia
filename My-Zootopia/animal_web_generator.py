import json

def load_data(file_path):

    with open(file_path, "r") as handle:
        return json.load(handle)

def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">\n'

    if "name" in animal_obj:
        output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    if "characteristics" in animal_obj and "diet" in animal_obj["characteristics"]:
        output += f'Diet: {animal_obj["characteristics"]["diet"]}<br/>\n'
    if "locations" in animal_obj and animal_obj["locations"]:
        output += f'Location: {animal_obj["locations"][0]}<br/>\n'
    if "characteristics" in animal_obj and "type" in animal_obj["characteristics"]:
        output += f'Type: {animal_obj["characteristics"]["type"]}<br/>\n'

    output += '</li>\n'

    return output

animals_data = load_data("animals_data.json")
output = ''
for animal in animals_data:
    output += serialize_animal(animal)

with open("animals_template.html", "r") as file:
    template = file.read()

new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as file:
    file.write(new_html)

print("zootopia animals.html successfully generated.")