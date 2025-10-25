from fastapi import FastAPI, HTTPException
from .database import get_all_students, get_student_by_id, create_student
from .schemas import Student, StudentCreate

app = FastAPI(title="Student API")


@app.get("/students", response_model=list[Student])
def list_students():
    return get_all_students()


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    student = get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Estudante nao encontrado")
    return student


@app.post("/students", response_model=Student, status_code=201)
def add_student(student: StudentCreate):
    return create_student(student)
