from lists.fonctions import execution_time
import random


def moyenne_etudiant(notes: dict):
  accumulator = 0
  for note in notes.values():
    accumulator += note
  return accumulator / len(notes)


def moyenne_classe(bulletins: dict):
  accumulator = 0
  for notes in bulletins.values():
    accumulator += moyenne_etudiant(notes)
  return accumulator / len(bulletins)


def moyenne_discipline(discipline: str, students: dict):
  accumulator = 0
  counter = 0
  for student in students.values():
    for note in student.items():
      if note[0] == discipline:
        accumulator += note[1]
        counter += 1
  if counter:
    return accumulator / counter
  raise ValueError('this discipline does not exists')


def best_student(bulletins: dict):
  students_average = []
  for notes in bulletins.values():
    students_average.append(moyenne_etudiant(notes))
  students_average.sort(reverse=True)
  return students_average[0]


def main():

  students = {
      'oui': {
          'math': random.randint(0, 20),
          'french': random.randint(0, 20),
          'physics': random.randint(0, 20),
          'sport': random.randint(0, 20),
          'english': random.randint(0, 20),
      },
      'alors': {
          'math': random.randint(0, 20),
          'french': random.randint(0, 20),
      },
      'franchement': {
          'math': random.randint(0, 20),
          'french': random.randint(0, 20),
          'sport': random.randint(0, 20),
      },
  }

  print(
      moyenne_etudiant(students['oui']),
      execution_time(moyenne_classe, students),
      execution_time(best_student, students),
      moyenne_discipline('math', students),
      sep='\n')


if __name__ == '__main__':
  main()
