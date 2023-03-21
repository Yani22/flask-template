from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS, cross_origin
from utils.format_response import format_response
from app.constants.status_codes import *
from app.constants.status_messages import *
from app.controllers.MaterialController import MaterialController

material = Blueprint('material', __name__)

@material.route('/get', methods=['GET'])
@cross_origin(origin='*')
def test_get():
    ret = MaterialController.get_materials()
    return jsonify(ret)

@material.route('/add', methods=['POST'])
@cross_origin(origin='*')
def test_post():
    req = request.get_json()
    ret = MaterialController.add_material(req['project_id'], req['material_name'], req['price'], req['quantity'])
    return jsonify(ret)

@material.route('/edit/<material_id>', methods=['PUT'])
@cross_origin(origin='*')
def test_put(material_id):
    req = request.get_json()
    ret = MaterialController.edit_material(material_id, req)
    return jsonify(ret)


@material.route('/delete/<material_id>', methods=['DELETE'])
@cross_origin(origin='*')
def test_delete(material_id):
    ret = MaterialController.delete_project(material_id)
    return jsonify(ret)
