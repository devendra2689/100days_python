import random

bingo = []

def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    #print(row)
    print(f"{row[0] } | {row[1]:^7} | {row[2]}")

numbers = []
for i in range(8):
  numbers.append(ran())

numbers.sort()

bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]

prettyPrint()
