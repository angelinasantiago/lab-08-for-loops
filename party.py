userinput = int(input("Let's party! How long until the party? (Give me a number.)"))
if (userinput < 1):
        print("PARTY NOW!!!")
else:
        for userinput in range(userinput, 0, -1):
          print(userinput)
        print("PARTY TIME!!!")
