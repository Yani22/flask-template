from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS, cross_origin
from utils.format_response import format_response
from app.constants.status_codes import *
from app.constants.status_messages import *
from app.controllers.ProjectDetailsController import ProjectDetailsController

project_details = Blueprint('project_details', __name__)

@project_details.route('/get', methods=['GET'])
@cross_origin(origin='*')
def test_get():
    ret = ProjectDetailsController.get_project_details()
    return jsonify(ret)

@project_details.route('/add', methods=['POST'])
@cross_origin(origin='*')
def test_post():
    req = request.get_json()
    ret = ProjectDetailsController.add_project_details(req['project_id'], req['engineer'], req['architect'],
                                                       req['project_manager'])
    return jsonify(ret)

@project_details.route('/edit/<projectdetails_id>', methods=['PUT'])
@cross_origin(origin='*')
def test_put(project_details_id):
    req = request.get_json()
    ret = ProjectDetailsController.edit_project_details(project_details_id, req)
    return jsonify(ret)


@project_details.route('/delete/<projectdetails_id>', methods=['DELETE'])
@cross_origin(origin='*')
def test_delete(project_details_id):
    ret = ProjectDetailsController.delete_project_details(project_details_id)
    return jsonify(ret)
