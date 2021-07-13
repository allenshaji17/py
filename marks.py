marks=[84,82,89,82,89]
Sum = 0
for i in range(0, len(marks)):
    Sum = Sum + marks[i]
avg = Sum/5
if (avg>75):
	print("distinction")
else:
    for i in marks:
        if (i < 45):
            print("failed")
            break
    else:
        print("passed")





