def collatz(number):
    if number%2 == 0:
        print(int(number//2))
        return number//2
    elif number%2 == 1:
        print(int(3*number + 1))
        return 3*number+1

def main():
    print("Enter a number:")
    my_number = input()
    while True:
        number_modified = collatz(int(my_number))
        if number_modified == 1:
            break
        else:
            my_number = number_modified

if __name__ == "__main__":
    main()
