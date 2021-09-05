from flask import Flask, jsonify, request, g
from config.Settings import Settings

import functools
import jwt

def loginRequired(func):
    @functools.wraps(func)
    def JWTCheck(*args, **kwargs):

        auth=True

        auth_header = request.headers.get('Authorization')
        print(auth_header)
        if auth_header: 
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
            auth=False

        if auth_token:
            print(auth_token)
            try:
                payload=jwt.decode(auth_token,Settings.secretKey,algorithms=['HS256'])
                
                email=payload['email']
                role=payload['role']
                
                g.email=email
                g.role=role
                

            except jwt.exceptions.InvalidSignatureError as err:
                print(err)
                auth=False

        if auth==False:
            return jsonify({"Message":"Not Authorized, Login Required"}),403

        value = func(*args, **kwargs)
        return value

    return JWTCheck

 
def adminRequired(func):
    @functools.wraps(func)
    def adminCheck(*args, **kwargs):
        print(g.role)
        if(g.role!="admin"):
            return jsonify({"Message":"Not Authorized, Admin Required"}),403

        value = func(*args, **kwargs)

        return value
    return adminCheck