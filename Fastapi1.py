from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "Name":"Alex",
        "Age": 23,
        "Year": 2000
    },
    2:{
        "Name":"Bob",
        "Age": 21,
        "Year": 2002
    }
}

class Student(BaseModel):
    Name : str
    Age : int
    Year : int

class UpdateStudent(BaseModel):
    Name : Optional[str]
    Age : Optional[int]
    Year : Optional[int]


@app.get("/")
def welcome():
    """This is a Welcome Page function"""
    try:
        return {"message": "hello!! Welcome."}
    except Exception as e:
        raise e

@app.get("/get-student/{std_id}")
def get_student(student_id:int):
    """This function will return the student details"""
    try:
        if student_id not in students:
            return {"Error": "Student ID does not exists."}

        return students[student_id]
    except Exception as e:
        raise e
    

@app.get("/get-by-name/{student_id}")
def get_student(*,student_id, name :Optional[str] = None):
    """This function take student id and name as input and return student details"""
    try:       
        for student in students:
            if students[student]["Name"] ==name:
                return students[student]
        return {"Data": "Not Found"}
    except Exception as e:
        raise e

@app.post('/create-student/{student_id}')
def create_student(student_id :int, student: Student):
    """This function will create new student"""

    try:
        if student_id in students:
            return {"Error": "Student ID is already exists."}
        students[student_id] = student
        return students[student_id]
    except Exception as e:
        raise e

@app.put("/update-student/{student_id}")
def update_student(student_id :int, student: UpdateStudent):
    """This function will update details of existing student"""

    try:
        if student_id not in students:
            return {"Error": "Student ID does not exists."}

        if student.Name != None:
            students[student_id].Name = student.Name
        if student.Age != None:
            students[student_id].Age = student.Age
        if student.Year != None:
            students[student_id].Year = student.Year
        return students[student_id]
    except Exception as e:
        raise e

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    """This function will delete the existing student"""
    try:
        if student_id not in students:
            return {"Error":"Student ID does not exists"}
        del students[student_id]
        return {"Message": "Student info is deleted sucessfully."}
    except Exception as e:
        raise e