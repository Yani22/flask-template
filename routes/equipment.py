from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS, cross_origin
from utils.format_response import format_response
from app.constants.status_codes import *
from app.constants.status_messages import *
from app.controllers.EquipmentController import EquipmentController

equipment = Blueprint('equipment', __name__)

@equipment.route('/get', methods=['GET'])
@cross_origin(origin='*')
def test_get():
    ret = EquipmentController.get_equipment()
    return jsonify(ret)

@equipment.route('/add', methods=['POST'])
@cross_origin(origin='*')
def test_post():
    req = request.get_json()
    ret = EquipmentController.add_equipment(req['project_id'], req['equipment_name'], req['price'], req['quantity'])
    return jsonify(ret)

@equipment.route('/edit/<equipment_id>', methods=['PUT'])
@cross_origin(origin='*')
def test_put(equipment_id):
    req = request.get_json()
    ret = EquipmentController.edit_equipment(equipment_id, req)
    return jsonify(ret)


@equipment.route('/delete/<equipment_id>', methods=['DELETE'])
@cross_origin(origin='*')
def test_delete(equipment_id):
    ret = EquipmentController.delete_equipment(equipment_id)
    return jsonify(ret)
