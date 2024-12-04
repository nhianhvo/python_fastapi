from fastapi import FastAPI, HTTPException , Request
from typing import Dict, List
from fastapi.responses import JSONResponse
from app.models.student import Student, StudentResponse
from app.services.grade_service import GradeService
from app.models.response_model import ResponseModel
from app.exceptions.custom_exceptions import StudentNotFoundError, InvalidGradesError, StudentAlreadyExistsError,StudentException
import logging


app = FastAPI(title="Student Management API")

@app.exception_handler(StudentException)
async def student_exception_handler(request: Request, exc: StudentException):
    return JSONResponse(
        status_code=exc.code,
        content={
            "code": exc.code,
            "status": "error",
            "message": exc.message,
            "data": None
        }
    )

# Thiết lập logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Lưu trữ tạm thời (trong thực tế nên dùng database)
students: List[Student] = []


@app.post("/students/", response_model=ResponseModel[StudentResponse])
async def add_student(student: Student):
    try:
        if any(s.name == student.name for s in students):
            raise StudentAlreadyExistsError(student.name)
        
        # Validate grades
        if not all(0 <= grade <= 10 for grade in student.grades):
            raise InvalidGradesError(student.grades)
        
        logger.info(f"Checking student: {student.name}")
        logger.info(f"Current students: {[s.name for s in students]}")
        
        students.append(student)
        result = GradeService.process_student_grades(student)
        
        # Tạo StudentResponse object
        return ResponseModel(
            code=201,
            status="success",
            message="Student added successfully",
            data=StudentResponse(
                name=student.name,
                info=result
            )
        )
        
    except StudentException as e:
        raise e
    except Exception as e:
        raise StudentException(str(e))
    
@app.patch("/students/{student_name}", response_model=StudentResponse)
async def update_student(student_name: str, student: Student):
    try:
        students[student_name] = student.grades
        results = GradeService.process_student_grades({student_name: student.grades})
        return ResponseModel(code=200, status="success", message="Student updated successfully", data=results[student_name])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# @app.get("/students/", response_model=ResponseModel[List[StudentResponse]])
# async def get_all_students():
#     if not students:
#         return ResponseModel(
#             code=200,
#             status="Success", 
#             message="No students",
#             data=[]  # Đảm bảo data là một list trống
#         )
    
#     results = GradeService.process_student_grades(students)
    
    
#     return ResponseModel(
#         code=200,
#         status="Success",
#         message="Get all students successfully",
#         data=[
#             StudentResponse(student=student.name, info=results[student.name])
#             for student in students
#             if student.name in results

#         ]
#     )
@app.get("/students/", response_model=ResponseModel[List[StudentResponse]])
async def get_all_students():
    # Sửa lại phần này, không gọi students như function
    if not students:  # Kiểm tra list rỗng
        return ResponseModel(
            code=200,
            status="success",
            message="No students found",
            data=[]
        )
    
    student_responses = []
    for student in students:
        try:
            result = GradeService.process_student_grades(student)
            student_responses.append(
                StudentResponse(
                    name=student.name,
                    info=result
                )
            )
        except Exception as e:
            print(f"Error processing student {student.name}: {str(e)}")
            continue
    
    return ResponseModel(
        code=200,
        status="success",
        message="Get all students successfully",
        data=student_responses
    )

@app.get("/students/{student_name}", response_model=ResponseModel[StudentResponse])
async def get_student(student_name: str):
    try:
        # Tìm học sinh và raise exception nếu không tìm thấy
        logger.info(f"Fr student: {student_name}")
        student = find_student(student_name)
        logger.info(f"student: {student}")
        result = GradeService.process_student_grades(student)
        logger.info(f"result: {result}")
        student_response = StudentResponse(
            name=student.name,
            info=result
        )
        
        logger.info(f"student_response: {student_response}")
        
        return ResponseModel(
            code=200,
            status="success",
            message="Get student successfully",
            data=student_response
        )
    except StudentException as e:
        raise e
    except Exception as e:
        raise StudentException(str(e))
    
# Helper function thay thế next()
def find_student(student_name: str) -> Student:
    for student in students:
        if student.name == student_name:
            return student
    raise StudentNotFoundError(student_name)