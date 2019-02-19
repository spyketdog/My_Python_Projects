def even_odds():
    n = input("Please enter a number: ").strip()
    try:
        if int(n) in range(2, 101, 2):
            print("Just an even number. ")
        elif int(n) >= 101:
            print("Cannot input numbers larger than 100 keep it smaller. ")
            even_odds()
        else:
            print("That's an odd number. ")
    except ValueError:
        print("Ooops please enter any single number like 1 or 2 or 333..try again. ")
        even_odds()

even_odds()
