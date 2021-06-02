#!/usr/bin/python3

"""
Script that lists all <states> from the database <hbtn_0e_0_usa>
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * from states")
    data = cursor.fetchall()
    for i in range(len(data)):
        if data[i][1].startswith('N'):
            print(data[i])
