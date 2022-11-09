#!/usr/bin/python3
"Lists all states where name matches the cmd argument"

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    datab = argv[3]
    name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd, db=datab)
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(name))

    results = cur.fetchall()
    for result in results:
        print(result)

    cur.close()
    db.close()
