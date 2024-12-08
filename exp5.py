name = input (" enter the student name:")
usn = input ("enter the student usn :" )

marks_subject1=float(input("enter marks in subject 1:"))
marks_subject2=float(input("enter marks in subject 2 :"))
marks_subject3=float(input("enter the marks in subject 3:"))

total_marks=marks_subject1 + marks_subject2 + marks_subject3
percentage=(total_marks/300)*100

print("student details:")
print("................")
print(f"name:{name}")
print(f"usn:{usn}")
print(f"marks_subject1:{marks_subject1}")
print(f"marks_subject2: {marks_subject2}")
print(f"marks_subject3 : {marks_subject3}")
print(f"total_marks : {total_marks}")
print(f"percentage:{percentage}")
