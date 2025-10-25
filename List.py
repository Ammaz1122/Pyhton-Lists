grades = (67,84,23, 23)
for item in grades[:]:
    if (item %2 == 0):
        print(item)


print(grades.count(23))

newGrades = grades + (90,) # its just concate the value only, should use , at the end while working with tupple
print(newGrades)