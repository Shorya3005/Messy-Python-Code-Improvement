name=input("Enter your name:")
age=int(input("Enter your age:"))
marks=int(input("Enter your marks:"))
if marks>=90:
 print("Excellent",name)
elif marks>=75:
 print("Very Good",name)
elif marks>=50:
 print("Good",name)
else:
 print("Needs Improvement",name)
print("Age:",age)
print("Marks:",marks)