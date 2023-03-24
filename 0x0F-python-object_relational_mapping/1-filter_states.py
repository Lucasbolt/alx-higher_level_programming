#!/usr/bin/python3
""" Lists all states with a name starting with \
        N from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` WHERE name REGEXP '^N' ORDER BY `id`")
    for state in c.fetchall():
        print(state)
    c.close()
    db.close()
