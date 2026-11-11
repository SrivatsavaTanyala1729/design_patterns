
from datetime import datetime


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "logs"):
            return
        self.logs = []

    def add_log(self, message):
        self.logs.append(message)
        print("Log added successfully.")

    def get_logs(self):
        return self.logs


class LoggerApplication:
    def __init__(self):
        self.logger = None

    def create_logger(self):
        existing = Logger._instance is not None
        self.logger = Logger()

        if existing:
            print("Using existing Logger instance.")
        else:
            print("New Logger instance created.")

    def log_message(self):
        if self.logger is None:
            print("Please create a Logger instance first!")
            return

        message = "Log entry at " + datetime.now().strftime("%H:%M:%S")
        self.logger.add_log(message)

    def display_logs(self):
        if self.logger is None:
            print("Please create a Logger instance first!")
            return

        print("\n===== LOGGER ENTRIES =====")

        for log in self.logger.get_logs():
            print(log)

    def menu(self):
        while True:
            print("\n===== SINGLETON LOGGER DEMO =====")
            print("1. Create Logger Instance")
            print("2. Add Log Message")
            print("3. Display Logs")
            print("4. Verify Singleton")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_logger()

            elif choice == "2":
                self.log_message()

            elif choice == "3":
                self.display_logs()

            elif choice == "4":
                a = Logger()
                b = Logger()
                print("Singleton Verified:", a is b)

            elif choice == "5":
                print("Exiting Logger Application.")
                break

            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = LoggerApplication()
    app.menu()
