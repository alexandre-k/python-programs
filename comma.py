def itemize(list):
    list.insert(-1, 'and')
    list_converted = list[0]
    for i in range(len(list)-3):
        list_converted = list_converted + ", " + list[i+1]
    list_converted = list_converted + " " + list[-2] + " " + list[-1]
    print(list_converted)

def main():
    list = ["cat", "dog", "lion", "girafe", "Mustang", "Porshe"]
    itemize(list)

if __name__ == "__main__":
    main()
