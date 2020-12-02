with open("input.txt") as i:
    intList = [int(line) for line in i.read().split()]


target = 2020

complement = 0

for i in intList:
  complement = target - i
  if complement in intList:
    print("{} and complement {}".format(i,complement))
    break
  else:
    print("Not found")


