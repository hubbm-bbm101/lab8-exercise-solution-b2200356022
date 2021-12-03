import sys

studentsText = open(sys.argv[1])
students = {}

for s in studentsText:
    name = s.strip("\n").split(":")[0]
    info = s.strip("\n").split(":")[1]
    students[name] = str(info)

namesInput = sys.argv[2].split(",")

for name in namesInput:
    try:
        print(f"Name: {name}, University: {students[name]}")
    except:
        print(f"No record of {name} was found")
