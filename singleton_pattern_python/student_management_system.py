
class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def query(self, sql):
        print("Executing:", sql)


class StudentModule:
    def __init__(self, database):
        self.database = database

    def execute(self):
        self.database.query("SELECT * FROM Students")


class FacultyModule:
    def __init__(self, database):
        self.database = database

    def execute(self):
        self.database.query("SELECT * FROM Faculty")


class ExaminationModule:
    def __init__(self, database):
        self.database = database

    def execute(self):
        self.database.query("SELECT * FROM Exams")


class UniversityApplication:
    def __init__(self):
        self.database = DatabaseManager()

        self.student = StudentModule(self.database)
        self.faculty = FacultyModule(self.database)
        self.examination = ExaminationModule(self.database)

    def student_module(self):
        self.student.execute()

    def faculty_module(self):
        self.faculty.execute()

    def exam_module(self):
        self.examination.execute()

    def verify_singleton(self):
        a = DatabaseManager()
        b = DatabaseManager()
        print("Singleton Verified:", a is b)

    def menu(self):
        while True:
            print("\n===== UNIVERSITY DATABASE MANAGER =====")
            print("1. Student Module")
            print("2. Faculty Module")
            print("3. Examination Module")
            print("4. Verify Singleton")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.student_module()

            elif choice == "2":
                self.faculty_module()

            elif choice == "3":
                self.exam_module()

            elif choice == "4":
                self.verify_singleton()

            elif choice == "5":
                print("Exiting Database Manager.")
                break

            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = UniversityApplication()
    app.menu()
