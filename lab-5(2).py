a = int(input("Enter three-degit num = "))
first = int(str(a)[0])
second = int(str(a)[1])
third = int(str(a)[2])



if first % 2 == 0 and  second % 2 == 0 and third % 2 == 0:
  print(first + second + third)
elif first % 2 == 0 and second % 2 == 0 and third % 2 == 1:
    print(first + second)
elif first % 2 == 0 and second % 2 == 1 and third % 2 == 0:
    print(first + third)
elif first % 2 == 1 and second % 2 == 0 and third % 2 == 0:
    print(second + third)
elif first % 2 == 0 and second % 2 == 1 and third % 2 == 1:
    print(first)
elif first % 2 == 1 and second % 2 == 0 and third % 2 == 1:
    print(second)
elif first % 2 == 1 and second % 2 == 1 and third % 2 == 0:
    print(third)
else:
    print("Nothing")
