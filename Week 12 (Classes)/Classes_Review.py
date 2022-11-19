class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)      

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
michael = Student("Michael Scott", 65)
jim = Student("Jim Halpert", 90)
pam = Student("Pam Beesly", 98)
pam.add_grade(Grade(100))
