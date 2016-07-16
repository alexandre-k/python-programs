users = [('Alexandre', 'Krispin', 'Alex'), ('Banana', 'Yoshimoto', 'Banana')]
for user in users:
    print('Adding user')
    username_cleaned = User.parse_strings(user[2])

    new_user = User.add((user[0], user[1], username_cleaned))
    print('Added', new_user.firstname, new_user.lastname, 'with username', new_user.username)
