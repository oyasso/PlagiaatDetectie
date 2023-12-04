from jinja2 import Environment, FileSystemLoader

auteurs = ["student_0", "student_1", "student_2"]  # lijst met anonieme studenten
auteurs_prive = {"Barbius": "student_0", "Justilius": "student_1", "Cervus": "student_2"}  # dict met echte namen

combos = {auteurs[i]: {auteurs[j]: [] for j in range(3)} for i in range(3)}  # dict comp
# dict om te renderen
context = {
    "studenten": combos
}

# manuele toevoeging van plagiaat_vormen
combos["student_0"]["student_0"] = "/"
combos["student_0"]["student_1"] = ["zelfde alinea"]
combos["student_0"]["student_2"] = ["Plagiaatvrij"]
combos["student_1"]["student_0"] = ["zelfde alinea"]
combos["student_1"]["student_1"] = "/"
combos["student_1"]["student_2"] = ["zelfde bronnen", "zelfde titel"]
combos["student_2"]["student_0"] = ["Plagiaatvrij"]
combos["student_2"]["student_1"] = ["zelfde bronnen", "zelfde titel"]
combos["student_2"]["student_2"] = "/"

# jinja setup
environment = Environment(loader=FileSystemLoader("templates/"))
output_template = environment.get_template("outputtemplate.html")
# write to file
with open("templates/outputtemplate.html", mode="w", encoding="utf-8") as o:
    o.write(output_template.render(context))
