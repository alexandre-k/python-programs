def search(mylist, value):
    if len(mylist) == 0:
        return False
    else:
        midpoint = len(mylist) // 2
    if mylist[midpoint] == value:
        print("found")
        return "found"
    elif mylist[midpoint] < value:
        return search(mylist[:midpoint], value)
    else:
        return search(mylist[midpoint + 1:], value)


def main():
    mylist = [ 2, 8, 14, 23, 27, 30, 43, 49, 67, 87, 93, 98 ]
    print(search(mylist, 93))
    print(search(mylist, 78))

if __name__ == "__main__":
    main()
