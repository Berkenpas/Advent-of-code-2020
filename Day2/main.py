file = open('input.txt', 'r') 
# Lines = file.readlines()

def puzzle1(file):
    count = 0

    #6-7 w: wwhmzwtwwk
    for line in file:
      step1 = line.split(":")
      password = step1[1]

      step2 = step1[0].split(" ")
      letter = step2[1]

      step3 = step2[0].split("-")
      min = step3[0]
      max = step3[1]

      print("password: ", password)
      
      print("letter: ", letter)
      
      print("Max: ", max, " min: ", min)
      
      if (password.count(letter) >= int(min)) and (password.count(letter) <= int(max)):
        count += 1
    print(count)

# puzzle1(file)

def puzzle2(file):
  count = 0

  for line in file:
      step1 = line.split(":")
      password = step1[1]

      step2 = step1[0].split(" ")
      letter = step2[1]

      step3 = step2[0].split("-")
      first = int(step3[0])
      second = int(step3[1])

      firstBool = password[first] == letter
      secondBool = password[second] == letter
    
      if (firstBool and not secondBool) or (secondBool and not firstBool):
       count += 1

  print(count)

puzzle2(file)