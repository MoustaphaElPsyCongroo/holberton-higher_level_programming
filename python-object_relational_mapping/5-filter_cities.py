#!/usr/bin/python3
"Lists all cities of input state"

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    datab = argv[3]
    state = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd, db=datab)
    cur = db.cursor()

    cur.execute(
        """SELECT cities.name FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id""", (state,))

    results = cur.fetchall()
    i = 0

    if len(results) == 0:
        print("")

    for result in results:
        for col in result:
            if i == len(results) - 1:
                print(col)
            else:
                print(col, end=", ")
            i += 1

    cur.close()
    db.close()
