import pickle


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"{self.name}, {self.age}, {self.address}")


class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)

        self.student_id = student_id
        self.grades = {}
        self.courses = []


    def add_grade(self, subject, grade):
        if subject in self.courses:
            self.grades[subject] = grade
        else:
            return True


    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)


    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Enrolled Courses: {self.courses}")
        print(f"Grades: {self.grades}")


class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor

        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
        else:
            return True
        
    def display_course_info(self):
        print("========== Course Information ==========")
        print(f"Course Name: {self.course_name}")
        print(f"Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        
        student_list = "Enrolled Students: "

        for student in self.students:
            student_list += f"{student}, "

        print(student_list)


class StudentManagementSystem:
    def __init__(self):
        self.Courses = {}
        self.Students = {}


    def add_new_student(self):
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        address = input("Enter Address: ")
        student_id = input("Enter Student id: ")

        if student_id in self.Students:
            print("Try another ID")
        else:
            student = Student(name, age, address, student_id)
            self.Students[student_id] = student
            print(f"Student {name} (ID: {student_id}) added successfully")


    def add_new_course(self):
        course_name = input("Enter Course Name: ")
        course_code = input("Enter Course Code: ")
        instructor_name = input("Enter Instructor Name: ")

        if course_code in self.Courses:
            print("Course Already Exists")
        
        else:
            course = Course(course_name,course_code,instructor=instructor_name)
            self.Courses[course_code] = course
            print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor_name}")


    def enroll_student_in_course(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")

        if student_id in self.Students and course_code in self.Courses:
            student = self.Students[student_id]
            course = self.Courses[course_code]
            enrolled = course.add_student(student.name)
            
            if enrolled:
                print(f"{student.name} (ID: {student_id}) is already Enrolled in {course.course_name} (Code: {course_code})")
            else:
                student.enroll_course(course.course_name)
                print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code})")
        else:
            print("Student id or Course code dosent exist.")


    def add_grade_for_student(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        grade = input("Enter Grade: ")

        if student_id in self.Students and course_code in self.Courses:
            student = self.Students[student_id]
            course = self.Courses[course_code]

            enrolled = student.add_grade(course.course_name, grade)

            if enrolled:
                print(f"{student.name} is not enrolled in {course.course_name} course.")
            else:
                print(f"Grade {grade} added for {student.name} in {course.course_name}")
        else:
            print("Student or Course dosent exists")


    def display_student_details(self):
        student_id = input("Enter Student ID: ")

        if student_id in self.Students:
            student_obj = self.Students[student_id]
            student_obj.display_student_info()
        else:
            print(f"No Students was found by (ID: {student_id})")


    def display_course_details(self):
        course_code = input("Enter Course Code: ")

        if course_code in self.Courses:
            course_obj = self.Courses[course_code]
            course_obj.display_course_info()
        else:
            print(f"No Course was found by (ID: {course_code})")


    def save_data(self):
        with open('students.pkl', 'wb') as file:
            pickle.dump(self.Students, file)

        with open('cources.pkl', 'wb') as file:
            pickle.dump(self.Courses, file)
        
        print("All student and course data saved successfully.")


    def load_data(self):
        try:
            with open('students.pkl', 'rb') as file:
                loaded_students = pickle.load(file)
            
            with open('cources.pkl', 'rb') as file:
                load_cources = pickle.load(file)
            
            self.Students = loaded_students
            self.Courses = load_cources

            print("Data loaded successfully.")
        
        except FileNotFoundError:
            print("File dosen't exists.")


def main():
    student_management_system = StudentManagementSystem()

    while True:
        print("===== Student Management System =====")
        print("""1. Add New Student\n2. Add New Course\n3. Enroll Student in Course\n4. Add Grade for Student\n5. Display Student Details\n6. Display Course Details\n7. Save Data to File\n8. Load Data from File\n0. Exit\n""")

        user_input = input("Select an Operation: ")

        try:
            user_input = int(user_input)
                
            if user_input == 0:
                break
            elif user_input == 1:
                student_management_system.add_new_student()
            elif user_input == 2:
                student_management_system.add_new_course()
            elif user_input == 3:
                student_management_system.enroll_student_in_course()
            elif user_input == 4:
                student_management_system.add_grade_for_student()
            elif user_input == 5:
                student_management_system.display_student_details()
            elif user_input == 6:
                student_management_system.display_course_details()
            elif user_input == 7:
                student_management_system.save_data()
            elif user_input == 8:
                student_management_system.load_data()
            else:
                raise ValueError

        except ValueError:
            print("Select a valid number from 0-8")


if __name__ == "__main__":
    main()
