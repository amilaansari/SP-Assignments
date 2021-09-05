from mysql.connector import pooling

class DatabasePool:

    connection_pool = pooling.MySQLConnectionPool(
                               pool_name="csp_pool",
                               pool_size=5,
                               host='localhost',
                               database='cspassignment',
                               user='root',
                               password='root')

    @classmethod
    def getConnection(cls): 
        dbConn = cls.connection_pool.get_connection()
        return dbConn
