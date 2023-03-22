from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS, cross_origin
from app.controllers.ProjectController import ProjectController
from app.models.Material import Material
from app.models.Project import Project
from app.models.Equipment import Equipment
from app.models.Manpower import Manpower
from app.models.ProjectDetails import ProjectDetails
from app import db

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


@project.route('/materials/<project_id>', methods=['GET'])
def get_project_materials(project_id):
    materials = db.session.query(Material.material_name, Material.price, Material.quantity,
                                  Project.name, Project.location) \
        .join(Project, Material.project_id == Project.id) \
        .filter(Material.project_id == project_id) \
        .order_by(Material.quantity.desc()) \
        .all()

    materials_list = []
    for m in materials:
        material_dict = {
            'material': m[0],
            'price': m[1],
            'quantity': m[2]
        }
        materials_list.append(material_dict)

    result_dict = {
        'name': materials[0][3],
        'location': materials[0][4],
        'materials': materials_list
    }

    return jsonify(result_dict)



@project.route('/equipments/<project_id>', methods=['GET'])
def get_project_equipments(project_id):
    query = db.session.query(Project.name, Project.location, Equipment.equipment_name,
                             Equipment.price, Equipment.quantity) \
        .join(Equipment, Project.id == Equipment.project_id) \
        .filter(Project.id == project_id) \
        .order_by(Equipment.price.desc()) \
        .all()

    equipments_dict = []
    for row in query:
        equipment_dict = {
            'equipment': row[2],
            'price': row[3],
            'quantity': row[4]
        }
        equipments_dict.append(equipment_dict)

    result_dict = {
        'name': query[0][0],
        'location': query[0][1],
        'equipments': equipments_dict
    }

    return jsonify(result_dict)




@project.route('/manpower/<project_id>', methods=['GET'])
def get_project_manpower(project_id):
    query = db.session.query(Project.name, Project.location, Manpower.manpower_name,
                             Manpower.position, Manpower.rate_per_hour) \
        .join(Manpower, Project.id == Manpower.project_id) \
        .filter(Project.id == project_id) \
        .order_by(Manpower.manpower_name.asc()) \
        .all()

    manpowers_dict = []
    for row in query:
        manpower_dict = {
            'manpower': row[2],
            'position': row[3],
            'rate': row[4]
        }
        manpowers_dict.append(manpower_dict)

    result_dict = {
        'name': query[0][0],
        'location': query[0][1],
        'manpower': manpowers_dict
    }

    return jsonify(result_dict)



@project.route('/details/<project_id>', methods=['GET'])
def get_project_details(project_id):
    project = db.session.query(Project, ProjectDetails).join(ProjectDetails).filter(Project.id == project_id).first()

    if not project:
        abort(404)

    material_count = Material.query.filter_by(project_id=project_id).count()
    equipment_count = Equipment.query.filter_by(project_id=project_id).count()
    manpower_count = Manpower.query.filter_by(project_id=project_id).count()

    result_dict = {
        'name': project.Project.name,
        'location': project.Project.location,
        'engineer': project.ProjectDetails.engineer,
        'architect': project.ProjectDetails.architect,
        'project_manager': project.ProjectDetails.project_manager,
        'material_count': material_count,
        'equipment_count': equipment_count,
        'manpower_count': manpower_count
    }

    return jsonify(result_dict)

