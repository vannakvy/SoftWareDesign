from person import Person
from course import Course
from aifc import Error


class Professor:
    def __inti__(self, first, last, dob, phone, address, salary):
        super().__init__(self, first, last, dob, phone, address)
        self.salary = salary
        self.courses = []
        self.got_raise = False

    def check_for_raise(self):
        if len(self.course) >= 4 and not self.got_raise:
            self.salary += 2000
            self.got_raise = True

    def add_course(self, course):
        if not isinstance(course, Course):
            raise Error("Invalid Course..")
        self.courses.append(course)
