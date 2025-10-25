studentList = [1,2,3,4]

if 5 in studentList:
    studentList.remove(4)
    print(studentList)
else:
    print("5 does not exists")

average = sum(studentList) / len(studentList)
print(average)