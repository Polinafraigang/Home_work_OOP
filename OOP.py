import self
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

        def _calc_average(self):
            total_grade = 0
            count_grade = 0
            for subbject_grade in self.grades.values():
                total_grade += sum(subbject_grade)
                count_grade += len(subbject_grade)
            return 0 if count_grade == 0 else total_grade / count_grade

        def __str__(self):
            return f'''Имя: {self.name}
    Фамилия: {self.surname}
    Средняя оценка за домашние задания: {self._calc_average()}
    Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
    Завершенные курсы: {", ".join(self.finished_courses)}'''

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calc_average() == other._calc_average()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calc_average() < other._calc_average()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}'''

@total_ordering
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return super().__str__() + f'\nСредняя оценка за лекции: {self._calc_average()}'

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calc_average() == other._calc_average()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calc_average() < other._calc_average()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def calc_average_grades_for_students(students, course):
    total_grade = 0
    count_grades = 0
    for student in students:
        grades = student.grades.get(course)
        if grades:
            total_grade += sum(grades)
            count_grades += len(grades)
    return total_grade / count_grades

def calc_average_grades_for_lecturers(lecturers, course):
    total_grade = 0
    count_grades = 0
    for lecturer in lecturers:
        grades = lecturer.grades.get(course)
        if grades:
            total_grade += sum(grades)
            count_grades += len(grades)
    return total_grade / count_grades

st1 = Student('Polina', 'Freigang', 'F')
st2 = Student('Dima', 'Medvedev', 'M')
rw1 = Reviewer('Victor', 'Popov')
rw2 = Reviewer('Oksana', 'Borovina')
lct1 = Lecturer('Tumur', 'Panov')
lct2 = Lecturer('Anna', 'Mrazish')

st1.courses_in_progress += ['Python', 'Java']
st2.courses_in_progress += ['Python', 'C++']

rw1.courses_attached += ['Python', 'Java']
rw2.courses_attached += ['C++', 'Java']

lct1.courses_attached += ['Python', 'Java']
lct2.courses_attached += ['C++', 'Java', 'Python']

rw1.rate_hw(st1, 'Python', 8)
rw1.rate_hw(st1, 'Python', 5)
rw1.rate_hw(st1, 'Python', 7)
rw1.rate_hw(st2, 'Python', 10)
rw1.rate_hw(st2, 'Python', 5)
rw1.rate_hw(st2, 'C++', 5)
rw1.rate_hw(st2, 'C++', 9)
rw2.rate_hw(st1, 'Python', 7)
rw2.rate_hw(st1, 'Java', 9)
rw2.rate_hw(st1, 'Java', 8)

st1.rate_lecture(lct1, 'Python', 6)
st1.rate_lecture(lct1, 'Python', 5)
st1.rate_lecture(lct2, 'Python', 4)
st1.rate_lecture(lct2, 'Python', 4)
st2.rate_lecture(lct2, 'C++', 5)
st1.rate_lecture(lct2, 'Java', 4)
st1.rate_lecture(lct2, 'Java', 5)

print(calc_average_grades_for_students([st1, st2],'Python'))
print(calc_average_grades_for_students([st1, st2],'Java'))
print(calc_average_grades_for_lecturers([lct1, lct2],'Python'))
print(calc_average_grades_for_lecturers([lct1, lct2],'Java'))