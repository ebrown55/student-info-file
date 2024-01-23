"""
A First Python Program: Collection of Student Data
Authors: Earl Brown, Micaela Ackerson
Date: 01/16/24
"""

class Student:
    """A class for students."""
    def __init__(self, last_name, first_name, student_number, age, major):
        self.last_name = last_name
        self.first_name = first_name
        self.student_number = student_number
        self.age = age
        self.major = major
        self.courses = []
        self.favorite_food = ' '

class Course:
    """A class for courses."""
    def __init__(self, subject_code, number, name, description):
        self.subject = subject_code
        self.number = number
        self.name = name
        self.description = description 
        self.students = []


def main():
    print()
    student_list = []
    course_list = []

    # create student objects, and append them to the students list
    a = Student('Law', 'Brian', 42, 18, 'CS')
    b = Student("Kripke", "Saul", 3425214353, 18, 'CS')
    c = Student('Brown', 'Earl', 900, 18, 'CS')
    student_list.append(a)
    student_list.append(b)
    student_list.append(c) 

    #create course objects, and append them to course list
    c1 = Course(0, 1, 'CS 135', 'An easy CS class')
    c2 = Course(1, 2, 'CS 128', 'A hard course, STAY AWAY')
    c3 = Course(2, 3, 'CS 127', 'Pretty easy, just pay attention')
    course_list.append(c1)
    course_list.append(c2)
    course_list.append(c3)


    #append courses to students
    for student in student_list:
        student.courses.append(c1.name)
        student.courses.append(c2.name) 
        student.courses.append(c3.name)
    
    #append students to courses
    for person in student_list:
        c1.students.append(person.first_name)
        c2.students.append(person.first_name)
        c3.students.append(person.first_name)
        

    # prints everyone name and the courses they have taken
    for student in student_list:
        print(f'{student.first_name} {student.last_name} ({student.major} major) is enrolled in {student.courses}')
    print()

    # prints all the students who have taken a specific course
    for course in course_list:
        print(f'All student who have taken {course.name}: {course.students}')
    print()

if __name__ == '__main__':
    main()