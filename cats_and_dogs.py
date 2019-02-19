def numCats():
    answers = input("How many cats do you have? ")
    try:
        if int(answers) >= 4:
            print("Thats a lot of cats.")
        elif int(answers) == 0:
            print("Not a cat person. I'am a dog person myself ;)")
        elif int(answers) <= -1:
            print("How can you have anything negative! Try again...Thank you.")
            numCats()
        else:
            print("That is just enough.")
    except ValueError:
        print("Ooops..You did not type a number. Try again....")
        numCats()

numCats()
