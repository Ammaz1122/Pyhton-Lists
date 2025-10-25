# numberList = [1,2,3]
# numberList[1] = 5 # in List we are assigning the value
# print(numberList)
"""
numberList = [1,5,6,7,9]

for item in numberList[:]:
    if(item % 2 == 1):
        numberList.remove(item)
        print(numberList)
else:
    print("No odd Number ")
    """
num = [1,2,3]
for item in num[:]:
    if (item % 2 ==0):
        print("Even Number in list")
        print(item)
