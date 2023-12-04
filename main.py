from jinja2 import Environment, FileSystemLoader
from pathlib import Path

dir = Path("alle_auteurs")

auteurs = {subdir.stem: {file.stem: file.read_text()} for subdir in dir.iterdir() for file in subdir.iterdir()}
auteurs_prive = {"Barbius": "student_0", "Justilius": "student_1", "Cervus": "student_2"}  # dict met echte namen

combos = {auteur: {student: "" for student in auteurs} for auteur in auteurs}  # dict comp
# dict om te renderen
context = {
    "studenten": combos
}

# plagiaat schrijven als file hetzelde is
for x in combos:
    for y in combos[x]:
        if combos[x][y] == combos[x]:
            combos[x][y] = "/"
        else:
            if auteurs[x] == auteurs[y]:
                combos[x][y] = "zelfde file"
            else:
                combos[x][y] = " "


# jinja setup
environment = Environment(loader=FileSystemLoader("templates/"))
output_template = environment.get_template("outputtemplate.html")
# write to file
with open("output.html", mode="w", encoding="utf-8") as o:
    o.write(output_template.render(context))
