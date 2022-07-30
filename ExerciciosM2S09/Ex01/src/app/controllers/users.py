from flask import Blueprint, request, jsonify

from src.app.db import db, User

users = Blueprint('users', __name__, url_prefix="/users")



@users.route("/", methods = ['GET'])
def list_users():
    return jsonify(db.all()), 200

@users.route("/<int:id>", methods = ["GET"])
def add_user(id):

    if id in db:

        return jsonify(db.get(doc_id=id)), 200
    
    else:
        return jsonify({"error": f"O id {id} não existe."}), 404
    
