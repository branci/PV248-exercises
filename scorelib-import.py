# PV248 Python, Skupina 2
# Part2 - Databases & SQL
# Branislav Smik

import re # regular expressions
import sqlite3

# windows database init
# sqlite3 scorelib.dat ".read scorelib.sql"

DATABASE = "scorelib.dat"
FILEPATH = "scorelib.txt"

# This is a base class for objects that represent database items. It implements
# the store() method in terms of fetch_id and do_store, which need to be
# implemented in every derived class (see Person below for an example).
class DBItem:
    def __init__( self, conn ):
        self.id = None
        self.cursor = conn.cursor()

    def store( self ):
        self.fetch_id()
        if ( self.id is None ):
            self.do_store()
            self.cursor.execute( "select last_insert_rowid()" )
            self.id = self.cursor.fetchone()[ 0 ]

# Example of a class which represents a single row of a single database table.
# This is a very simple example, since it does not contain any references to
# other objects.
class Person( DBItem ):
    def __init__( self, conn, string ):
        super().__init__( conn )
        self.name = re.sub( '\([0-9+-]+\)', '', string )
        self.years = re.findall('\((\d{4})-*(\d{4})\)', string)

    def fetch_id( self ):
        self.cursor.execute( "select id from person where name = ?", (self.name,) )
        self.id = self.cursor.fetchone()
        res = self.cursor.fetchone()
        if not res is None:
            self.id = res[0]

    def do_store( self ):
        #if years are not present, insert only name
        if self.years.__len__() == 0:
            self.cursor.execute( "insert into person (name) values (?)", (self.name,) )
        else:
            self.cursor.execute("insert into person (born, died, name) values (?, ?, ?)", (int(self.years[0][0]),
                                                                                           int(self.years[0][1]), self.name))

class Score( DBItem ):
    def __init__(self, conn, string):
        super.__init__( conn )
        self.name = None
        self.genre = None
        self.key = None
        self.incipit = None
        self.year = None

    def fetch_id( self ):
        self.cursor.execute( "select id from score where name = ?", (self.name,) )
        self.id = self.cursor.fetchone()
        res = self.cursor.fetchone()
        if not res is None:
            self.id = res[0]

    def do_store( self ):
        pass

def main():
    conn = sqlite3.connect(DATABASE)
    rx = re.compile(r"(.*): (.*)")
    for line in open(FILEPATH, 'r', encoding='utf-8'):
        m = rx.match(line)
        if m is None: continue
        k = m.group(1)
        v = m.group(2)
        if k == 'Composer' or k == 'Editor':
            for c in v.split(';'):
                p = Person(conn, c.strip())
                p.store()

    conn.commit()

if __name__ == "__main__":
    main()