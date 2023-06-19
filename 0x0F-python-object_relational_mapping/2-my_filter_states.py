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
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=database)
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id"
    cur.execute(query.format(state_name))
    table = cur.fetchall()

    for row in table:
        print(row)

    cur.close()
    conn.close()
