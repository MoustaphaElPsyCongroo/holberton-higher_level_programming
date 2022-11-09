#!/usr/bin/python3
"Lists all states from the database hbtn_0e_0_usa"
from sys import argv
import MySQLdb

user = argv[1]
passwd = argv[2]
datab = argv[3]

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd, db=datab)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
