from flask import Flask, jsonify, request
from flask_cors import CORS
from model.Menu import Menu

app = Flask(__name__)
CORS(app)


#1: Retrieve all Menu Items, 
@app.route('/menu', methods=["GET"])
def getMenu():
    try:
        menu= Menu.getAllMenu()
        jsonUsers={"menuItems": menu}
        return jsonify(jsonUsers),200

    except Exception as err:
        print(err)
        return {},500

#2a: Retrieve all Menu Items, sort by price DESC
@app.route('/menu/desc', methods=["GET"])
def getMenuDESC():
    try:
        menu= Menu.getAllMenuDESC()
        jsonUsers={"menuItems": menu}
        return jsonify(jsonUsers),200

    except Exception as err:
        print(err)
        return {},500

#2b: Retrieve all Menu Items, sort by price ASC
@app.route('/menu/asc', methods=["GET"])
def getMenuASC():
    try:
        menu= Menu.getAllMenuASC()
        jsonUsers={"menuItems": menu}
        return jsonify(jsonUsers),200

    except Exception as err:
        print(err)
        return {},500

#3: Retrieve Menu Items based on searchInput
@app.route('/menu/search/<stall_name>', methods=["GET"])
def getMenuItem(stall_name):
    try:
        menuItem= Menu.getMenuItem(stall_name)
        jsonUsers={"menuItems": menuItem}
        return jsonify(jsonUsers),200

    except Exception as err:
        print(err)
        return {},500

#4a: Retrieve Menu Items based on searchInput, sort by price DESC
@app.route('/menu/search/desc/<stall_name>', methods=["GET"])
def getMenuItemDESC(stall_name):
    try:
        menuItem= Menu.getMenuItemDESC(stall_name)
        jsonUsers={"menuItems": menuItem}
        return jsonify(jsonUsers),200

    except Exception as err:
        print(err)
        return {},500

#4b: Retrieve Menu Items based on searchInput,sort by price ASC
@app.route('/menu/search/asc/<stall_name>', methods=["GET"])
def getMenuItemASC(stall_name):
    try:
        menuItem= Menu.getMenuItemASC(stall_name)
        jsonUsers={"menuItems": menuItem}
        return jsonify(jsonUsers),200

    except Exception as err:
        print(err)
        return {},500

if __name__ == "__main__":
    app.run(debug=True)
