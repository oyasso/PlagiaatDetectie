from pathlib import Path
import json

dir = Path("alle_auteurs")

for subdir in dir.iterdir():
    for file in subdir.iterdir():
        if file.is_file():
            print(file.stem)

auteurs = [subdir.stem for subdir in dir.iterdir()]
auteurs2 = {subdir.stem: {file.stem: file.read_text()} for subdir in dir.iterdir() for file in subdir.iterdir()}
combos = {auteur: {student: [] for student in auteurs} for auteur in auteurs}  # dict comp

print(auteurs2)
print(json.dumps(combos, indent=4))
