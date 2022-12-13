from ..lists.fonctions import execution_time
import random


def moyenneEtudiant(notes: dict):
  accumulator = 0
  for note in notes.values():
    accumulator += note
  return accumulator / len(notes)


def moyenneClasse(bulletins: dict):
  accumulator = 0
  for notes in bulletins.values():
    accumulator += moyenneEtudiant(notes)
  return accumulator / len(bulletins)


def bestStudent(bulletins: dict):
  students_average = []
  for notes in bulletins.values():
    students_average.append(moyenneEtudiant(notes))
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
      moyenneEtudiant(students['oui']),
      execution_time(moyenneClasse, students),
      execution_time(bestStudent, students),
      sep='\n')


if __name__ == '__main__':
  main()
