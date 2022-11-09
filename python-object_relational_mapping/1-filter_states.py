#!/usr/bin/python3
"Lists all states with a name starting with N"

from sys import argv
import MySQLdb

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    datab = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd, db=datab)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    results = cur.fetchall()

    for result in results:
        print(result)

    cur.close()
    db.close()
