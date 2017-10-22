# PV248 Python, Group 2
# Part 3 - SQL Redux & JSON
# Branislav Smik
# 16.10.2017
#
# INPUT: Print ID as argument
# OUTPUT: List of composers for the print ID

import re # regular expressions
import sqlite3
import json
import sys


# DB file to pull data from
DATABASE = "scorelib_rockai_final.dat"

def print_composers(cursor, print_id):
    # order of joins: print-edition-score-scoreauthor-person
    cursor.execute("SELECT person.name FROM person JOIN score_author on person.id=score_author.composer \n "
                   "JOIN score on score_author.score=score.id \n "
                   "JOIN edition on score.id=edition.score \n "
                   "JOIN print on edition.id=print.edition \n "
                   "WHERE print.id=(?)", (print_id,))
    composers = cursor.fetchall()
    has_multiple_composers = False if composers.__len__()==1 else True
    print("Composer{suffix} for print number {id}:".format(suffix='s' if has_multiple_composers else '',
                                                           id=print_id))
    for composer in composers:
        print(composer[0])

def main():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    print_composers(cursor, sys.argv[1])

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()