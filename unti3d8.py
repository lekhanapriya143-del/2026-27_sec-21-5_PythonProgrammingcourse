# Example solution: student details with **kwargs
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_details(name="priya", maths=85, science=90)
