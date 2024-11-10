sum = 0
students = []
userFlag = "Y"
feedbackAvail = "Y"
while userFlag == "Y":
    student = {}
    student["name"] = input("Enter the nme of student : ")
    feedbackAvail = input("Is Feedback Available (Y / N) : ")
    if feedbackAvail:
        student["feedback"] = feedback = int(input("Enter your feedback : "))
    userFlag = input("Do you want to continue (Y / N) : ")
    sum=sum+feedback
    students.append(student)
avg = sum/len(students)
if(avg>4):
    print("Very good")
elif(avg>3):
    print("Average feedback is  average")
elif(avg>2):
    print("average feedback is bad")
else:
    print("replace the teacher")
print(students)
print("#########Feedback of the students#########")
name = input("Enter the name of student : ")
studentAvail = False
for i in range(0, len(students)):
    if students[i]["name"] == name:
        studentAvail = True
        break
if studentAvail:
    print("the name of the student is",students[i]["name"])
    print("the feedback of the student is",students[i]["feedback"])
else:
    print("Student not foud")
