# i want to take student name,total number of subjects,subject name,marks in a subject and total marks obtained overall by  a student. 
# i want to assign a grade on the basis of total marks obtained by a student


# taking student name as input
student = (input("name of student: "))
# taking subject name as input
subjects  = int(input("enter number of subject:"))
# making a python dictionary of the marks_dict
marks_dict ={}
# putting loop for iteration
for subject in range(subjects):
      #  it will take marks as input
    subject_name = (input("enter name of subject:"))
    marks = int(input(f"Enter marks for {subject_name}: "))  # Using subject name in prompt
    marks_dict[subject_name]=marks
total_marks = sum(marks_dict.values())  # Sum of all marks
percentage = (total_marks / (subjects * 100)) * 100
print("=================MARKSHEET GENERATED SUCCESSFULLY=================")
print("Total Marks:", total_marks)
print("percentage:",percentage)
         
if marks>=91 and marks<=100:
    print("Your Grade is A1")

elif marks>=81:
    print("your grade is A")
elif marks>=71:
    print("your grade is B")
elif marks>=61:
    print("your grade is C")
elif marks>=51:
    print("your grade is D")
else:
      print("fail")
      print("So sorry! you've failed,but don't be afraid to learn from mistakes and try again")

print("=====================================================================")

