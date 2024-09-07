from flask import Blueprint, request, jsonify

ch = Blueprint("test", __name__, url_prefix="/test")

@ch.route("/data")
def process_data():
    return jsonify({"message": "ok"})

@ch.route('/test')
def method_name():
    return  jsonify({"message": "ok"})

@ch.route('/test2')
def method_name():
    return  jsonify({"message": "ok"})