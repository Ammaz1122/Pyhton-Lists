from datetime import datetime # first datetime is the module and second datetime is the class

# day = datetime.now()
# # print(day.strftime("%A")) # string format time %A showig Day Name


# month = datetime(1996,11,1)
# print(month.strftime("%B") + day.strftime("%Y"))


birthday = datetime(1996,11,1)

print(birthday.strftime("%d %B %Y"))