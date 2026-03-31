class Course:
    def __init__(self, code, title, capacity):
        self.code = code
        self.title = title
        self.capacity = capacity
        self.students = []

    def is_full(self):
        return len(self.students) >= self.capacity

    def enroll(self, student_id):
        if self.is_full():
            return False, "Course is full"
        if student_id in self.students:
            return False, "Already enrolled"
        self.students.append(student_id)
        return True, "Enrolled successfully"

    def drop(self, student_id):
        if student_id not in self.students:
            return False, "Not enrolled"
        self.students.remove(student_id)
        return True, "Dropped successfully"


class Student:
    def __init__(self, student_id):
        self.id = student_id
        self.courses = []

    def enroll(self, course):
        success, msg = course.enroll(self.id)
        if success:
            self.courses.append(course.code)
        return success, msg

    def drop(self, course):
        success, msg = course.drop(self.id)
        if success:
            self.courses.remove(course.code)
        return success, msg


# Sample data
courses = {
    "CS101": Course("CS101", "Intro to Programming", 2),
    "CS201": Course("CS201", "Data Structures", 2)
}

student = Student("STU001")


def show_courses():
    print("\nAvailable Courses:")
    for c in courses.values():
        print(f"{c.code} - {c.title} ({len(c.students)}/{c.capacity})")


def main():
    while True:
        print("\n=== MENU ===")
        print("1. View Courses")
        print("2. Register Course")
        print("3. Drop Course")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_courses()

        elif choice == "2":
            show_courses()
            code = input("Enter course code: ").upper()
            if code in courses:
                success, msg = student.enroll(courses[code])
                print(msg)
            else:
                print("Course not found")

        elif choice == "3":
            code = input("Enter course code: ").upper()
            if code in courses:
                success, msg = student.drop(courses[code])
                print(msg)
            else:
                print("Course not found")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
