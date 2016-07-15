with open('db.txt', 'r') as userdb:

    for row in userdb:
        newuser = User(username=row[1],
                       firstname=row[2],
                       lastname=row[3],
                       )
