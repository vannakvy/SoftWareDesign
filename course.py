from professor import Professor
from aifc import Error
from typing import List
from enroll import Enroll


class Course:
    def __init__(self, name, code, min, max, professor):
        self.name = name
        self.code = code
        self.max = max
        self.min = min
        self.professors = []
        self.enrollments = []

        if isinstance(professor, Professor):
            self.professors.append(professor)
        elif isinstance(professor, List):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise Error("Invalid Professor")
            self.professors = professor
        else:
            raise Error(" Invalid Professor..")

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise Error("Invalid Professor ")
        self.professors.append(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise Error(" Invalid Enroll")
        if len(enrollments) == self.max:
            raise Error("Cannot enroll, Course is full...")
        self.enrollments.append(enroll)

    def is_cancelled(self):
        return len(self.enrollments) < self.min
