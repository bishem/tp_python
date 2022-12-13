from typing import Any


def main():
  empty = []
  print(empty)

  not_empty: list[Any] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(not_empty)
  print(len(not_empty))

  not_empty[3] = 'hallo'
  print(not_empty)

  not_empty.remove(7)
  print(not_empty)

  not_empty.insert(6, 'much obliged')
  print(not_empty)


  [print(value) for value in not_empty]

  for value in not_empty:
      print(value)

  counter = 0
  while counter < len(not_empty):
      print(not_empty[counter])
      counter += 1

  for counter in range(len(not_empty)):
      print(not_empty[counter])

if __name__ == '__main__':
    main()