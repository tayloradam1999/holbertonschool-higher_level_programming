#!/usr/bin/python3

"""
Lists all cities from the database
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    with db.cursor() as cursor:
        cursor.execute("""
            SELECT
                cities.name
            FROM
                states
            JOIN
                cities
            ON
                states.id = cities.state_id
            WHERE
                states.name = BINARY %(states)s
            """, {
                'states': argv[4]
            })
        data = cursor.fetchall()
    if len(data) == 0:
        print("")
    for i in range(len(data)):
        if i != len(data) - 1:
            print("{}, ".format(data[i][0]), end="")
        else:
            print(data[i][0])
