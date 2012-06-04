import sys

from com.ziclix.python.sql import zxJDBC

DATABASE    = "solarsys.db"
JDBC_URL    = "jdbc:sqlite:%s"  % DATABASE
JDBC_DRIVER = "org.sqlite.JDBC"

def getConnection(jdbc_url, driverName):
    """
        Given the name of a JDBC driver class and the url to be used 
        to connect to a database, attempt to obtain a connection to 
        the database.
    """

    try:
        # no user/password combo needed here, hence the None, None
        dbConn = zxJDBC.connect(jdbc_url, None, None, driverName)
    except zxJDBC.DatabaseError, msg:
        print msg
        sys.exit(-1)

    return dbConn

if __name__ == "__main__":
    print zxJDBC
    print('Hello Jython')
    dbConn = getConnection(JDBC_URL, JDBC_DRIVER)
    print dbConn
    
    print "testing"

