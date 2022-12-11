import random
import time


def moyenneEtudiant(notes: dict):
    accumulator = 0
    for note in notes.values():
        accumulator += note
    return accumulator / len(notes)


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
    },
}

print(moyenneEtudiant(students['oui']))

max = 0
moyenne = 0
accumulator = 0
sink = []
bulletins = students.values()

begin = time.time()

for notes in bulletins:
    accumulator += moyenneEtudiant(notes)
    sink.append(moyenneEtudiant(notes))

moyenne = accumulator / len(bulletins)
sink.sort(reverse=True)
max = sink[0]

elapsed = time.time() - begin

print(elapsed)
print(moyenne)
print(max)
