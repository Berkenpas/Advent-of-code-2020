with open("input.txt") as i:
    intList = [int(line) for line in i.read().split()]


target = 2020

complement = 0

flagCheck = False

for i in intList:
  if flagCheck:
    break
  else:
    for j in intList:
      firstTwo = i + j
      complement = target - firstTwo
      if complement in intList:
        print("{} and complement {} and {}".format(i,j,complement))
        flagCheck = True
        break
      else:
        print("Not found")
