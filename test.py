studenten = {
    "student_0": {
        "student_0": "/",
        "student_1": " "
    },
    "student_1": {
        "student_0": " ",
        "student_1": "/"
    }
}

for student in studenten:
    print(studenten.get(student).get("student_1", "Not Found"))
