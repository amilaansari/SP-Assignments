from model.DatabasePool import DatabasePool
from config.Settings import Settings

import datetime
import jwt

class User:

#1: Verify Admin Credentials
    @classmethod
    def getUser(cls, email, password):
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from user where email = %s and password = binary %s"
            cursor.execute(sql,(email,password))
            user=cursor.fetchall()
             
            print (len(user))
            return user
        
        finally:
            dbConn.close()

#A2- 7: Login Authentication with JWT   
    @classmethod
    def loginUser(cls, email, password):
        try: 
            dbConn=DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql="select * from user where email=%s and password= binary %s"
            cursor.execute(sql,(email,password))
            user=cursor.fetchall()

            if len(user) == 1:
                user=user[0]
                payload={"email": user["email"], "role":user["role"],"exp":datetime.datetime.utcnow() + datetime.timedelta(seconds=7200)}
                key=jwt.encode(payload, Settings.secretKey, algorithm="HS256")
                return {"jwt":key}

            else:
                return {"jwt":""}

        finally:
            dbConn.close()