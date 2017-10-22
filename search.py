# PV248 Python, Group 2
# Part 3 - SQL Redux & JSON
# Branislav Smik
# 16.10.2017
#
# INPUT: Composer name / substring of a name
# OUTPUT: List of composers for the given name, together with all of their scores

import re # regular expressions
import sqlite3
import json
import sys


# DB file to pull data from
DATABASE = "scorelib_rockai_final.dat"

def composers_scores(cursor, composer_sub):
    output = {}
    composer_sub_sql = '%' + composer_sub + '%'
    cursor.execute("SELECT person.name FROM person WHERE person.name like (?)", (composer_sub_sql,))
    composers = cursor.fetchall()
    for composer in composers:
        cursor.execute("SELECT score.name FROM score JOIN score_author on score.id=score_author.score \n "
                       "JOIN person on person.id=score_author.composer WHERE person.name==(?)", (composer[0],))
        scores = cursor.fetchall()
        output[composer[0]] = [score[0] for score in scores]

    json.dump(output, sys.stdout, indent=4)

def main():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    composer_sub = sys.argv[1]
    composers_scores(cursor, composer_sub)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()