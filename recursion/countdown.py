def countdown(number):
    if number == 0:
        print("The End")
    else:
        print(number)
        countdown(number - 1)


countdown(10)
