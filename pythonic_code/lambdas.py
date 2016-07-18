def main():
    print(find_special_numbers(check_for_odd))
    print(find_special_numbers(lambda x: x % 6 == 1))

    list_of_words = ['CPython', 'read', 'Please', 'improvements', 'issues.', 'on', 'comprehensions', 'user-facing', 'of']
    print('Before sorting', list_of_words)
    list_of_words.sort()
    print('After sorting', list_of_words)
    list_of_words.sort(key=lambda w: w.lower())
    print('With lower()', list_of_words)



def find_special_numbers(special_selector, limit=10):
    found = []
    n = 0
    while len(found) < limit:
        if special_selector(n):
            found.append(n)
        n += 1
    return found

def check_for_odd(n):
    return n % 2 == 1

if __name__ == "__main__":
    main()
