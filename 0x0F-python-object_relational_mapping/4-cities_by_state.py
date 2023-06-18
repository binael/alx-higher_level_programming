#!/usr/bin/python3

"""A python script that employs the module MySQLdb to list
the data in a database
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=database)
    cur = conn.cursor()
    query = "SELECT c.id, s.name, c.name FROM cities AS c\
        INNER JOIN states AS s ON c.state_id = s.id ORDER BY c.id"

    cur.execute(query)
    table = cur.fetchall()

    for row in table:
        print(row)
