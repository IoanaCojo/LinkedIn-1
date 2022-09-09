
def whileContinue():
  i = 0
  while i < 6:
    i += 1
    if i == 3:
      continue # skipps the next line
    print(i)
whileContinue()

print('\n')
def whileBreak():
  i = 1
  while i < 6:
    print(i)
    if i == 3:
      break
    i += 1

whileBreak()