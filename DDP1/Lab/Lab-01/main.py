# Name: Franky Raymarcell Sinaga
# NPM: 23xxxxxxxx
# TA Code: XXX

# Take input for student's name
# And change into title-case
name = input("Enter name: ").title()

# Take input for three exams
exam1 = input("Enter the score for Exam 1: ")
exam2 = input("Enter the score for Exam 2: ")
exam3 = input("Enter the score for Exam 3: ")

# Calculate the average and total exam
total_exam = int(exam1) + int(exam2) + int(exam3)
average_exam = total_exam / 3

# Take the total seconds as input
total_seconds = int(input("Enter the total seconds taken for the exams: "))

# Calculate the hours, minutes, and remaining seconds
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# Format the time
time_format = str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) + " seconds"

# Detail information about student's name and exam
print("---", name, "---")
print("Exam Scores:", exam1 + ", " + exam2 + ", " + exam3)
print("Total Score:", total_exam)
print("Average Score:", f"{average_exam:.2f}")
print("Time Taken:", time_format)
print()
# Feedback message for student
print("---", "Message for", name, "---")
print("Hey,", name, end=". ")
print("You got exam scores of", exam1 + ", " + exam2 + ", and " + exam3, "with total of", total_exam, "and average of", f"{average_exam:.2f}", end=". ")
print("The total time taken is", time_format, end=". ")
print()