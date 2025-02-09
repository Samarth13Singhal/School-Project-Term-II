stu_data = {}
l = int(input("Enter the total number of students: "))

for i in range(l):
    name = input("Enter the name of the student: ")
    marks = int(input("Enter the marks of the student: "))
    roll_no = int(input("Enter the roll number of the student: "))
    stu_data[roll_no] = [name, marks]

print("The student data is in the following format:- ")
print("Roll No.\t| Name\t\t| Marks")

for i in stu_data:
    print(f"{i}\t\t| {stu_data[i][0]}\t\t| {stu_data[i][1]}")