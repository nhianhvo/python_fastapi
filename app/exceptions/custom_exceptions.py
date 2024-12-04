class StudentException(Exception):
    """Base exception for student operations"""
    def __init__(self, message: str, code: int = 500):
        self.message = message
        self.code = code
        super().__init__(self.message)

class StudentNotFoundError(StudentException):
    """Raised when student is not found"""
    def __init__(self, student_name: str):
        super().__init__(
            message=f"Student {student_name} not found",
            code=404
        )

class StudentAlreadyExistsError(StudentException):
    """Raised when trying to add an existing student"""
    def __init__(self, student_name: str):
        super().__init__(
            message=f"Student {student_name} already exists",
            code=400
        )

class InvalidGradesError(StudentException):
    """Raised when grades are invalid"""
    def __init__(self, grades: list):
        super().__init__(
            message=f"Invalid grades: {grades}. Grades must be between 0 and 10",
            code=400
        ) 