import random


def main():
  print(random.randint(0, 5000))
  print(random.randrange(0, 100000000, 21))
  print(random.choice(range(0, 100000000)))
  numbers = list(range(0, 10))
  print(numbers)
  random.shuffle(numbers)
  print(numbers)


if __name__ == '__main__':
  main()
