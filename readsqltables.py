import mysql
from mysql.connector import errorcode
class readsqltables(object):
    def __init__(self):
        self.data=0
        self.TABLES={}
        self.projectlist=[]
        self.fundlist=[]
        self.projectlinkslist=[]
    def readprojectfundview(self):
        try:

            cnx = mysql.connector.connect(user='root', password='QAzx.1ws', host='127.0.0.1',
                                          database='gtr_organisations')
            cursor = cnx.cursor()

            self.TABLES['projectview'] = ("SELECT * FROM gtr_organisations.projectview")
            self.TABLES['fundview'] = ("SELECT * FROM gtr_organisations.fundview")
            self.TABLES['[projectlinkview'] = ("SELECT * FROM gtr_organisations.projectlinkview")
            cursor.execute(self.TABLES['projectview'])

            # Make sure data is committed to the database
            results = cursor.fetchall()
            for row in results:
                projectview=dict()
                projectview['id'],projectview['title'],projectview['grantCategory'],projectview['LeadOrganisation'],projectview['identifier']=row[0],row[1],row[2],row[3],row[4]
                self.projectlist.append(projectview)

            cursor.execute(self.TABLES['fundview'])

            resultsb = cursor.fetchall()
            for row in resultsb:
                fundview=dict()
                fundview['id'],fundview['created'],fundview['start'],fundview['end'],fundview['amount']=row[0],row[1],row[2],row[3],row[4]
                self.fundlist.append(fundview)

            cursor.execute(self.TABLES['projectlinkview'])

            resultsc = cursor.fetchall()
            for row in resultsc:
                projectlinkview=dict()
                projectlinkview['id'],projectlinkview['rel_id'],projectlinkview['rel']=row[0],row[1],row[2]
                self.projectlinkslist.append(projectlinkview)


            cursor.close()
            cnx.close()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
        else:
            print("successfully connected to mysql database")

        return self.projectlist,self.fundlist,self.projectlinkslist
