marks=[99,99,99,99,44]
Sum = 0
for i in range(0,len(marks)):
    Sum = Sum + marks[i]
avg = Sum/len(marks)
fail = False
for i in marks:
    if (i < 45):
        fail = True
        print("failed")

if (avg > 75) and fail != True:
    print("distinction")
else:
    print("passed")
    







    




