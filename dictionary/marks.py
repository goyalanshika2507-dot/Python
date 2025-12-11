students={"aastha":85,"aryan":90,"riya":78}
students["mohit"]=88
students["aastha"]=92
del students["riya"]
name="aryan"
if name in students:
    print(f"{name}'s marks:",students[name])
else:
    print("student not found")
print("all students",students)
print("names",list(students.keys()))
print("marks",list(students.values()))
print("name-marks pairs",list(students.items()))