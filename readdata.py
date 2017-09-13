import mysql
from mysql.connector import errorcode

class readdatac:
    def __init__(self):
        self.TABLES=dict()
        self.personlist=list()
        self.isislist=list()
        self.data=self.readsqltable()

    def readsqltable(self):
        try:

            cnx = mysql.connector.connect(user='root', password='QAzx.1ws', host='127.0.0.1',
                                          database='gtr_organisations')
            cursor = cnx.cursor()

            self.TABLES['personview'] = ("SELECT * FROM gtr_organisations.personview")
            self.TABLES['isisview'] = ("SELECT * FROM isisdb.isisview")
            cursor.execute(self.TABLES['personview'])

            # Make sure data is committed to the database
            results = cursor.fetchall()
            for row in results:
                personview=dict()
                personview['firstname'],personview['othername'],personview['surname'],personview['name']=row[0],row[1],row[2],row[3]
                self.personlist.append(personview)

            cursor.execute(self.TABLES['isisview'])

            resultsb = cursor.fetchall()
            for row in resultsb:
                isisview=dict()
                isisview['initials'],isisview['firstname'],isisview['givenname'],isisview['familyname'],isisview['organisationname']=row[0],row[1],row[2],row[3],row[4]
                self.isislist.append(isisview)


            cursor.close()
            cnx.close()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
        else:
            print("successfully connected to mysql database")


