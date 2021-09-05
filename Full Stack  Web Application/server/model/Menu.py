from model.DatabasePool import DatabasePool

class Menu:
    #1: Retrieve all Menu Items
    @classmethod
    def getAllMenu(cls):
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from menu"
            cursor.execute(sql)
            result=cursor.fetchall()

            return result

        finally:
            dbConn.close()
    
    #2a: Retrieve all Menu Items, sort by price DESC
    @classmethod
    def getAllMenuDESC(cls):
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from menu order by price desc"
            cursor.execute(sql)
            result=cursor.fetchall()

            return result

        finally:
            dbConn.close() 

    #2b: Retrieve all Menu Items, sort by price ASC
    @classmethod
    def getAllMenuASC(cls):
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from menu order by price asc"
            cursor.execute(sql)
            result=cursor.fetchall()

            return result

        finally:
            dbConn.close()
             
    #3: Retrieve Menu Items based on searchInput
    @classmethod
    def getMenuItem(cls,stall_name):
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from menu where stall_name like %s"
            cursor.execute(sql,(("%"+stall_name+"%"),))
            result=cursor.fetchall()

            return result

        finally:
            dbConn.close()
    
    #4a: Retrieve Menu Items based on searchInput, sort by price DESC
    @classmethod
    def getMenuItemDESC(cls,stall_name):
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from menu where stall_name like %s order by price desc"
            cursor.execute(sql,(("%"+stall_name+"%"),))
            result=cursor.fetchall()

            return result

        finally:
            dbConn.close()
    
    #4b: Retrieve Menu Items based on searchInput,sort by price ASC
    @classmethod
    def getMenuItemASC(cls,stall_name):
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from menu where stall_name like %s order by price asc"
            cursor.execute(sql,(("%"+stall_name+"%"),))
            result=cursor.fetchall()

            return result

        finally:
            dbConn.close()
    
