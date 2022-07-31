from flask import Blueprint, request, jsonify

from src.app.db import db
from src.app.utils import exists_key

users = Blueprint('users', __name__, url_prefix="/users")



@users.route("/", methods = ['GET'])
def list_users():
    return jsonify(db.all()), 200

@users.route("/<int:id>", methods = ["GET"])
def find_user_id(id):

    user = db.get(doc_id=id)

    if user:
        return {"Usuario procurado": user}, 200

    else:
        return jsonify({"error": f"O id {id} não existe."}), 404
    
@users.route("/create", methods = ['POST'])
def create_user():

    list_keys = ['nome', 'email', 'cpf']

    data = exists_key(request.get_json(), list_keys)

    if 'error' in data:
        return jsonify(data), 400
    
    else:
        insert = db.insert(data)

        return {"id": insert, "user": data}, 202

@users.route("/delete/<string:id>", methods = ["DELETE"])
def delete_user():
    pass
    