from logging import log
from re import L
from flask import Flask, jsonify, request
from flask_cors import CORS
from model.Menu import Menu
from model.Category import Category
from model.User import User
from validation.Validator import *

app = Flask(__name__)
CORS(app)

#1: Verify Admin Credentials/get User
@app.route('/user/<email>,<password>',methods=["GET"])
def getUser(email,password):
    try:
        user=User.getUser(email,password)
        if len(user) == 1:
            message = "Valid Email and Password"
        else:
            message = "Invalid Email and/or Password"
        
        return jsonify(message),200 

    except Exception as err:
        print(err)
        return {},500

#A2- 7: Login Authentication with JWT
@app.route('/user/login',methods=["POST"])
def loginUser():
    try:
        userJSON=request.json 

        jwtResult=User.loginUser(userJSON["email"],userJSON['password']) 

        return jsonify(jwtResult),200

    except Exception as err:
        print(err)
        return {},500

#2: Add New Menu Item, Admin Only
@app.route('/menu',methods=["POST"])
@loginRequired
@adminRequired
def insertMenu():
    try:
        userJSON=request.json

        rows=Menu.insertMenu(userJSON['name'],
                            userJSON['description'],
                            userJSON['price'],
                            userJSON['stall_name'],
                            userJSON['ImageURL'],
                            userJSON['CategoryId'],
                            userJSON['DateInserted'])
   
        message={"Rows Affected":rows}
        return jsonify(message),200    

    except Exception as err:
        print(err)
        return {},500

#3: Add New Category, Admin Only
@app.route('/category',methods=["POST"])
@loginRequired
@adminRequired
def insertCategory():
    try:
        userJSON=request.json

        rows=Category.insertCategory(userJSON['name'],
                            userJSON['description'])
   
        message={"Rows Affected":rows}
        return jsonify(message),200    

    except Exception as err:
        print(err)
        return {},500


#4: Retrieve all Menu Items
@app.route('/menu',methods=["GET"])
@loginRequired
def getMenu():
    try:
        menu= Menu.getAllMenu()
        jsonUsers={"menus": menu}
        return jsonify(jsonUsers),200

    except Exception as err:
        print(err)
        return {},500

#5: Retrive Menu Items based on Stall Name substring
@app.route('/menu/<stall_name>',methods=["GET"])
@loginRequired
def getMenuItem(stall_name):
    try:
        menuItem= Menu.getMenuItem(stall_name)
        jsonUsers={"menuItems": menuItem}
        return jsonify(jsonUsers),200

    except Exception as err:
        print(err)
        return {},500

#6: Retrieve all Categories
@app.route('/category',methods=["GET"])
@loginRequired
def getCategory():
    try:
        category= Category.getAllCategories()
        jsonUsers={"categories": category}
        return jsonify(jsonUsers),200

    except Exception as err:
        print(err)
        return {},500

#A2- 8: Update Menu, Admin Only
@app.route('/menu/<int:menuID>',methods=["PUT"])
@loginRequired
@adminRequired
def updateMenu(menuID):
    try:
        userJSON=request.json 

        rows=Menu.updateMenu(userJSON['name'], userJSON['description'], userJSON['price'], userJSON['stall_name'], userJSON['ImageURL'], userJSON['CategoryId'], userJSON ['DateInserted'], menuID)
   
        message={"Rows Affected":rows}
        return jsonify(message),200    

    except Exception as err:
        print(err)
        return {},500

#A2- 9: Delete Category, Admin Only
@app.route('/category/<int:categoryId>',methods=["DELETE"])
@loginRequired
@adminRequired
def deleteCategory(categoryId):
    try:
        rows=Category.deleteCategory(categoryId)
        message={"Rows Affected":rows}
        return jsonify(message),200    

    except Exception as err:
        print(err)
        return {},500

#A2- 10: Delete Menu, Admin Only (extra)
@app.route('/menu/<int:menuID>',methods=["DELETE"])
@loginRequired
@adminRequired
def deleteMenuItem(menuID):
    try:
        rows=Menu.deleteMenuItem(menuID)
        message={"Rows Affected":rows}
        return jsonify(message),200    

    except Exception as err:
        print(err)
        return {},500

#A2- 11: Update Category, Admin Only (extra)
@app.route('/category/<int:categoryId>',methods=["PUT"])
@loginRequired
@adminRequired
def updateCategory(categoryId):
    try:
        userJSON=request.json 

        rows=Category.updateCategory(userJSON['name'], userJSON['description'], categoryId)
   
        message={"Rows Affected":rows}
        return jsonify(message),200    

    except Exception as err:
        print(err)
        return {},500


#Run App
if __name__ == '__main__': 
    app.run(debug=True)
