class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I am {self.age} years old."


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"Hi, I'm {self.name}, age {self.age}, student ID: {self.student_id}."


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"Hi, I'm {self.name}, age {self.age}, I teach {self.subject}."


if __name__ == "__main__":
    alice     = Student("Alice",     17, "S001")
    mr_smith  = Teacher("Mr. Smith", 45, "Mathematics")

    print(alice.introduce())
    print(mr_smith.introduce())