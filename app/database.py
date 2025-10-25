from .schemas import Student

students_db = [
    Student(id=1, name="Renato Hioji Okamoto Odake", 
            email="renato@example.com")
]


def get_all_students():
    return students_db


def get_student_by_id(student_id: int):
    return next((s for s in students_db if s.id == student_id), None)


def create_student(student):
    new_id = max(s.id for s in students_db) + 1 if students_db else 1
    new_student = Student(id=new_id, **student.dict())
    students_db.append(new_student)
    return new_student
