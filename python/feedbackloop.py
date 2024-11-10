sum = 0
i = 0
while i < 5:
    sum += int(input("Feedback "+str(i+1)+": "))
    i+=1
avg = sum/5
if(avg>5):
    print('good')
elif avg > 3:
    print("avarage")
else:
    print("bad")