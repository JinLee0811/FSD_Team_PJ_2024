import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import pickle
import threading
from utils import logger

class SingletonMeta(type):
    _instances = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self):
        # 실행 중인 스크립트의 절대 경로를 기준으로 파일 경로를 설정합니다.
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.filename = os.path.join(base_dir, "data", "students.data")
        self.students = self.load_students()

    # 나머지 메서드들...

    def load_students(self):
        try:
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            return []

    def save_students(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.students, f)

    def get_student_by_email(self, email):
        return next(
            (student for student in self.students if student.email == email), None
        )

    def get_student_by_id(self, student_id):
        return next(
            (student for student in self.students if student.student_id == student_id),
            None,
        )

    def add_student(self, student):
        if not self.get_student_by_email(student.email) and not self.get_student_by_id(
            student.student_id
        ):
            self.students.append(student)
            self.save_students()
        else:
            print(Fore.BLUE + f"Student {student.email} already exists")

    def update_student(self, student):
        found = False
        for idx, s in enumerate(self.students):
            if s.student_id == student.student_id:
                self.students[idx] = student
                found = True
                break
        if found:
            self.save_students()
        else:
            print("Student not found.")

    def remove_student_by_id(self, student_id):
        original_len = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]
        if len(self.students) < original_len:
            self.save_students()
            return True  # 학생이 성공적으로 제거되었을떄
        return False  # 학생이 목록에 없어 제거되지 않았을떄

    def get_all_students(self):
        return self.students

    def clear_all(self):
        self.students = []
        self.save_students()

    def remove_student_by_email(self, email):
        original_len = len(self.students)
        self.students = [s for s in self.students if s.email != email]
        if len(self.students) < original_len:
            self.save_students()
            
    def print_all_students(self):
        students = self.get_all_students()
        for student in students:
            print(f"Email: {student.email}, Name: {student.name}, Student ID: {student.student_id}")   
            
    def log_students(self):
        students = self.get_all_students()
        for student in students:
            logger.info(f"Email: {student.email}, Name: {student.name}, Student ID: {student.student_id}")
            

class Student:
    def __init__(self, email, password, name, student_id):
        self.email = email
        self.password = password
        self.name = name
        self.student_id = student_id
        self.subjects = []