from model.DatabasePool import DatabasePool

class Menu:

#4: Retrieve all Menu Items
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

#5: Retrive Menu Items based on Stall Name substring
    @classmethod
    def getMenuItem(cls, stall_name):
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from menu where stall_name like %s order by price asc"
            cursor.execute(sql,(("%"+stall_name+"%"),))
            result=cursor.fetchall()

            return result

        finally:
            dbConn.close()

#2: Add New Menu Item, Admin Only
    @classmethod
    def insertMenu(cls, name, description, price, stall_name, ImageURL, CategoryId, DateInserted):
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="insert into menu(name,description,price,stall_name,ImageURL,CategoryId,DateInserted) values(%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,(name,description,price,stall_name,ImageURL,CategoryId,DateInserted)) 
            dbConn.commit()

            rows=cursor.rowcount
            print(cursor.lastrowid)

            return rows
        
        finally:
            dbConn.close()

#A2- 8: Update Menu, Admin Only
    @classmethod
    def updateMenu(cls, name, description, price, stall_name, ImageURL, CategoryId, DateInserted, menuID):
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="update menu set name = %s, description = %s, price = %s, stall_name = %s , ImageURL = %s, CategoryId = %s , DateInserted = %s where menuID = %s"
            cursor.execute(sql,(name, description, price, stall_name, ImageURL, CategoryId, DateInserted, menuID) )
            dbConn.commit()

            rows=cursor.rowcount

            return rows
        
        finally:
            dbConn.close()

#A2- 10: Delete Menu, Admin Only (extra)
    @classmethod
    def deleteMenuItem(cls, menuID):
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="delete from menu where menuID=%s"
            cursor.execute(sql,(menuID,))
            dbConn.commit()

            rows=cursor.rowcount

            return rows
        
        finally:
            dbConn.close()     
    
    