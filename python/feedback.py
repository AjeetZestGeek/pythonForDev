f1 = int(input("Feedback 1: "))
f2 = int(input("Feedback 2: "))
f3 = int(input("Feedback 3: "))
f4 = int(input("Feedback 4: "))
f5 = int(input("Feedback 5: "))
avg = (f1+f2+f3+f4+f5)/5
if(avg>5):
    print('good')
elif avg > 3:
    print("avarage")
else:
    print("bad")