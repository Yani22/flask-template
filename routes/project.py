from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS, cross_origin
from utils.format_response import format_response
from app.constants.status_codes import *
from app.constants.status_messages import *
from app.controllers.ProjectController import ProjectController

project = Blueprint('project', __name__)

@project.route('/get', methods=['GET'])
@cross_origin(origin='*')
def test_get():
    ret = ProjectController.get_projects()
    return jsonify(ret)

@project.route('/add', methods=['POST'])
@cross_origin(origin='*')
def test_post():
    req = request.get_json()
    ret = ProjectController.add_project(req['project_name'], req['location'])
    return jsonify(ret)

@project.route('/edit/<project_id>', methods=['PUT'])
@cross_origin(origin='*')
def test_put(project_id):
    req = request.get_json()
    ret = ProjectController.edit_project(project_id, req)
    return jsonify(ret)


@project.route('/delete/<project_id>', methods=['DELETE'])
@cross_origin(origin='*')
def test_delete(project_id):
    ret = ProjectController.delete_project(project_id)
    return jsonify(ret)
