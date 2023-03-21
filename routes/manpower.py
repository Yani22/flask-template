from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS, cross_origin
from utils.format_response import format_response
from app.constants.status_codes import *
from app.constants.status_messages import *
from app.controllers.ManpowerController import ManpowerController

manpower = Blueprint('manpower', __name__)

@manpower.route('/get', methods=['GET'])
@cross_origin(origin='*')
def test_get():
    ret = ManpowerController.get_manpower()
    return jsonify(ret)

@manpower.route('/add', methods=['POST'])
@cross_origin(origin='*')
def test_post():
    req = request.get_json()
    ret = ManpowerController.add_manpower(req['project_id'], req['manpower_name'], req['position'],
                                          req['rate_per_hour'])
    return jsonify(ret)

@manpower.route('/edit/<manpower_id>', methods=['PUT'])
@cross_origin(origin='*')
def test_put(manpower_id):
    req = request.get_json()
    ret = ManpowerController.edit_manpower(manpower_id, req)
    return jsonify(ret)


@manpower.route('/delete/<manpower_id>', methods=['DELETE'])
@cross_origin(origin='*')
def test_delete(manpower_id):
    ret = ManpowerController.delete_manpower(manpower_id)
    return jsonify(ret)
