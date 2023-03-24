#!/usr/bin/python3
"""
Displays all cities of a given state from the
states table of the database hbtn_0e_4_usa.
Safe from SQL injections.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost'
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]])
    c.close()
    db.close()
