from typing import List
from app.models.student import Student, StudentResult

class GradeService:
    @staticmethod
    def process_student_grades(student: Student) -> StudentResult:
        # Kiểm tra và xử lý grades
        if not student.grades:
            return StudentResult(average=0.0, rank="Chưa có điểm")
        
        # Tính điểm trung bình
        average = sum(student.grades) / len(student.grades)
        
        # Xếp loại
        if average >= 9.0:
            rank = "Xuất sắc"
        elif average >= 8.0:
            rank = "Giỏi"
        elif average >= 7.0:
            rank = "Khá"
        else:
            rank = "Trung bình"
        
        return StudentResult(
            average=round(average, 2),
            rank=rank
        )