from model.DatabasePool import DatabasePool

class Category:

#6: Retrieve all Categories
    @classmethod
    def getAllCategories(cls):
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from category"
            cursor.execute(sql)
            result=cursor.fetchall()

            return result

        finally:
            dbConn.close()
    
#3: Add New Category, Admin Only
    @classmethod
    def insertCategory(cls,name,description): 
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="insert into category(name,description) values(%s,%s)"
            cursor.execute(sql,(name,description)) 
            dbConn.commit()

            rows=cursor.rowcount
            print(cursor.lastrowid)

            return rows
        
        finally:
            dbConn.close()

#A2- 9: Delete Category, Admin Only
    @classmethod
    def deleteCategory(cls, categoryId):
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="delete from category where categoryId=%s"; "delete from menu where CategoryId=%s"
            cursor.execute(sql,(categoryId,))
            dbConn.commit()

            rows=cursor.rowcount

            return rows
        
        finally:
            dbConn.close()   

#A2- 11: Update Category, Admin Only (extra)
    @classmethod
    def updateCategory(cls, name, description, categoryId):
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="update category set name = %s, description = %s where categoryId = %s"
            cursor.execute(sql,(name, description, categoryId))
            dbConn.commit()

            rows=cursor.rowcount

            return rows
        
        finally:
            dbConn.close()
