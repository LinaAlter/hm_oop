def __lt__(self, other):
    return self.grades < other.gredes

def __eq__(self, other):
    return self.grade == other.grade



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lect(self, lecturer, course, grade):
        
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]         
        else:
            return 'Ошибка'
        
    def __average_grade(self): 
        grades_count = 0 
        for grade in self.grades:
            grades_count += len(self.grades[grade]) 
            average_s = sum(map(sum, self.grades.values())) / grades_count 
            return average_s
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.__average_grade()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}')  
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
   

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
        
        
    def rate_hw(self, student, course, grade):
           if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
               if course in student.grades:
                   student.grades[course] += [grade]
               else:
                student.grades[course] = [grade]
           else:
                return 'Ошибка'
    
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}')      

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        

    def __average_grade(self): 
        grades_count = 0 
        for grade in self.grades:
            grades_count += len(self.grades[grade]) 
            average_l = sum(map(sum, self.grades)) / grades_count 
            return average_l    
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_grade()}')   
# Lecturer 1
lecturer_1 = Lecturer('Олег', 'Булыгин')
lecturer_1.courses_attached = 'Основы'
# Lecturer 2
lecturer_2 = Lecturer('Алена', 'Батицкая')
lecturer_2.courses_attached = ['Git']
# Lecturer 3
lecturer_3 = Lecturer('Тимур', 'Анвартдинов')
lecturer_3.courses_attached = ['ООП']
# Student 1
student_1 = Student('Надежда', 'Баскакова', 'женский')
student_1.rate_lect(Lecturer, 'ООП', [7, 8, 9, 6, 10])
student_1.courses_in_progress += ['ООП']
student_1.finished_courses = ['Основы', 'Git']
# Student 2
student_2 = Student('Даврон', 'Акрамов', 'мужской')
student_2.rate_lect(Lecturer, ['Git', 'Основы'], [9, 9, 8, 6, 8])
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Основы']
# Student 3
student_3 = Student ('Алиса', 'Нуриева', 'женский')
student_3.rate_lect(Lecturer,'Основы', [4, 6, 8, 6, 9])
student_3.courses_in_progress += ['Основы']
student_3.finished_courses = None


reviewer = Reviewer('Александр', 'Бардин')
reviewer.rate_hw(student_1, 'Fullstack', [5, 8, 9, 7, 9])
reviewer.rate_hw(student_2, 'Frontend', [8, 6 , 9, 6, 8,])
reviewer.rate_hw(student_3, 'Fullstack', [8, 9, 5, 8 ,7])

print(student_2)
print(lecturer_1)
