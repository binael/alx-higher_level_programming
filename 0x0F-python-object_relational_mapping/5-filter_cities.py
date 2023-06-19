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
    state_name = sys.argv[4].split(';')[0]

    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=database)
    cur = conn.cursor()
    query = "SELECT c.name FROM cities AS c LEFT JOIN states AS s\
        ON c.state_id = s.id WHERE BINARY s.name = '{}'\
        ORDER BY c.id ASC".format(state_name)

    cur.execute(query)
    table = cur.fetchall()

    flag = False

    for row in table:
        if flag:
            print(", ", end="")
        print(row[0], end="")
        flag = True

    print("")
    cur.close()
    conn.close()
