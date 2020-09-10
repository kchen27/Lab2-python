#Author: Kyle Chen kvc5823@psu.edu
#Collaborator:
#Collaborator:
#Collaborator:
#Collaborator:
#Section: 10R
#Breakout: 16

def LetterGrade(grade):
  if grade >= 93.0:
    grade = "A"
  elif grade >= 90.0:
    grade = "A-"
  elif grade >= 87.0:
    grade = "B+"
  elif grade >= 83.0:
    grade = "B"
  elif grade >= 80.0:
    grade = "B-"
  elif grade >= 77.0:
    grade = "C+"
  elif grade >= 70.0:
    grade = "C"
  elif grade >= 60.0:
    grade = "D"
  else:
    grade = "F"
  return grade

def run():
  grade = input("Enter your CMPSC 131 grade: ")
  grade = float(grade)
  lg = LetterGrade(grade)
  print (f"Your letter grade for CMPSC 131 is {lg}.")

if __name__ == "__main__":
  run()