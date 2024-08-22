class Instructor:
    def __init__(self, instructor_name, address):
        self.name = instructor_name  # Corrected to store instructor_name in self.name
        self.address = address  # Store address in self.address

instructor_1 = Instructor("Jenny", "Rishi")
print(type(instructor_1))