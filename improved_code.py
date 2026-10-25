def get_student_details():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    marks = int(input("Enter your marks: "))
    return name, age, marks


def display_result(name, age, marks):
    if marks >= 90:
        performance = "Excellent"
    elif marks >= 75:
        performance = "Very Good"
    elif marks >= 50:
        performance = "Good"
    else:
        performance = "Needs Improvement"

    print("\nStudent Details")
    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)
    print("Performance:", performance)


name, age, marks = get_student_details()
display_result(name, age, marks)