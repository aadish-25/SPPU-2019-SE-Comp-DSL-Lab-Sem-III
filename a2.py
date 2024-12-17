'''
Problem Statement: Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency
'''

def average_score(N, absent, marks):
    sum = 0
    for mark in marks:
        if mark != -1:
            sum = sum + mark
    average = sum / (N - absent)
    print("The average of the class is :" + str(average))

def highest_lowest(marks):
    highest = marks[0]
    lowest = 999999999
    for mark in marks:
        if mark >= highest:
            highest = mark
        if mark <= lowest and mark != -1:
            lowest = mark
    print(f"The highest score of the class is {highest} and the lowest score of the class is {lowest}")

def absent_students(ab):
    print(f"The number of absent students is {ab}")

def highest_freq(marks):
    freq = {}
    for mark in marks:
        if mark in freq:
            freq[mark] += 1
        else:
            freq[mark] = 1
    highest_marks = None
    highest_freq = 0

    for mark, count in freq.items():
        if count > highest_freq:
            highest_marks = mark
            highest_freq = count
    print(f"The mark value of {highest_marks} has the highest frequency of {highest_freq}")

def main():
    marks = []

    print("Enter total number of students : ")
    N = int(input())	

    absent_count = 0

    print("Enter the marks for each student. Enter -1 if absent")
    for i in range(N):		
        mark = int(input())
        marks.append(mark)
        if mark == -1:
            absent_count += 1
	
    print(f"The marks of students are : {marks}")

    # MENU
    while True:
        print("\nMenu:")
        print("1. Calculate Average Score")
        print("2. Calculate Highest and Lowest Score")
        print("3. Count of Absent Students")
        print("4. Display Mark with Highest Frequency")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            average_score(N, absent_count, marks)
        elif choice == 2:
            highest_lowest(marks)
        elif choice == 3:
            absent_students(absent_count)
        elif choice == 4:
            highest_freq(marks)
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
