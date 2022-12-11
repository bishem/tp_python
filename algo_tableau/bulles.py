import math
import random
from re import L
from typing import Any


def index_minimum(tableau: list[int], left: int, right: int):
  # sink = tableau.copy()
  # sink.sort()
  # return tableau.index(sink[0])
  return tableau[left] if tableau[left] < tableau[right] else tableau[right]


def bubble_sort(tableau: list[int]):
  for down in range(len(tableau)-1, 0, -1):
    sorted = True
    print(tableau)
    for up in range(down):
      if tableau[up] > tableau[up+1]:
        tableau[up], tableau[up+1] = tableau[up+1], tableau[up]
        sorted = False
    if sorted:
      break


def search_matching_in(probe: int, tableau: list[int]):
  for element in tableau:
    if probe < element:
      return 'not in the list'
    if probe == element:
      return f'exists at index {tableau.index(element)} of list'


def search_with_dichotomy_matching_in(probe: int, tableau: list[int]):
  pool = tableau.copy()

  while len(pool) > 1:
    half_length = len(pool) // 2
    if probe < tableau[half_length]:
      pool = pool[:half_length]
    else:
      pool = pool[half_length:]
    print(pool)

  if probe is not pool[0]:
    return 'not in the list'
  else:
    return f'exists at index {tableau.index(pool[0])} of list'


def insert(element: int, tableau: list[int]):

  pass


sink = []
limit = 10
pool = range(limit)
for _ in pool:
  sink.append(random.randint(0, limit**2))

random.shuffle(sink)


print(sink)
print(index_minimum(sink, 2, 8))
bubble_sort(sink)
print(search_with_dichotomy_matching_in(50, sink))
