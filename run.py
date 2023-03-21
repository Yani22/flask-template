from app import app
from app.models import import_models
from scripts import import_scripts
# from flask_seeder import FlaskSeeder
from routes import register_blueprints
from flask import request, jsonify
from app.models.Material import Material
from app.models.Project import Project
from app.models.Equipment import Equipment
from app.models.Manpower import Manpower
from app.models.ProjectDetails import ProjectDetails
from sqlalchemy.orm import joinedload


@app.route('/', methods=['GET'])
def index():
    return "THIS!! IS!! SPARTAAAAA!! charottt!! <3"


@app.route('/project/materials/<project_id>', methods=['GET'])
def get_project_materials(project_id):
    # Get project details
    project = Project.query.get_or_404(project_id)

    # Get materials for the project, sorted by quantity in descending order
    materials = Material.query.filter_by(project_id=project_id)\
                              .order_by(Material.quantity.desc())\
                              .all()

    # Construct a list of dictionaries containing material details
    materials_list = []
    for material in materials:
        material_dict = {
            'material': material.material_name,
            'price': material.price,
            'quantity': material.quantity
        }
        materials_list.append(material_dict)

    # Construct the result dictionary
    result_dict = {
        'name': project.name,
        'location': project.location,
        'materials': materials_list
    }

    # Return the result as JSON
    return jsonify(result_dict)


@app.route('/project/equipments/<project_id>', methods=['GET'])
def get_project_equipments(project_id):
    # Retrieve project details
    project = Project.query.get_or_404(project_id)

    # Retrieve equipment details for the project
    equipment = Equipment.query.options(joinedload(Equipment.project))\
        .filter_by(project_id=project_id)\
        .order_by(Equipment.price.desc())\
        .all()

    # Create a list of dictionaries containing equipment details
    equipments_dict = []
    for e in equipment:
        equipment_dict = {
            'equipment': e.equipment_name,
            'price': e.price,
            'quantity': e.quantity
        }
        equipments_dict.append(equipment_dict)

    # Create the response dictionary
    result_dict = {
        'name': project.name,
        'location': project.location,
        'equipments': equipments_dict
    }

    # Return the response as JSON
    return jsonify(result_dict)


@app.route('/project/manpower/<project_id>', methods=['GET'])
def get_project_manpower(project_id):
    # Get the project details
    project = Project.query.get_or_404(project_id)

    # Get the manpower details for the project and order by manpower name
    manpower = Manpower.query.filter_by(project_id=project_id).order_by(Manpower.manpower_name.asc()).all()

    # Create a dictionary for the manpower details
    manpowers_dict = [{'manpower': m.manpower_name, 'position': m.position, 'rate': m.rate_per_hour} for m in manpower]

    # Create a result dictionary with project details and manpower dictionary
    result_dict = {
        'name': project.name,
        'location': project.location,
        'manpower': manpowers_dict
    }

    # Return the result as a JSON response
    return jsonify(result_dict)


@app.route('/project/details/<project_id>', methods=['GET'])
def get_project_details(project_id):
    # Get project and project details
    project = Project.query.get_or_404(project_id)
    details = ProjectDetails.query.filter_by(project_id=project_id).first()

    # Get counts for materials, equipment, and manpower
    material_count = Material.query.filter_by(project_id=project_id).count()
    equipment_count = Equipment.query.filter_by(project_id=project_id).count()
    manpower_count = Manpower.query.filter_by(project_id=project_id).count()

    # Create dictionary for response
    result_dict = {
        'name': project.name,
        'location': project.location,
        'engineer': details.engineer,
        'architect': details.architect,
        'project_manager': details.project_manager,
        'material_count': material_count,
        'equipment_count': equipment_count,
        'manpower_count': manpower_count
    }

    # Return response as JSON
    return jsonify(result_dict)


# configuration settings
def configure():
    import_models()
    import_scripts()
    register_blueprints()


# run configuration settings
configure()

if __name__ == "__main__":
    debug = True
    app.run(debug=True, host="0.0.0.0", port=5000)
    # socket.run(app, debug=debug, host='0.0.0.0', port=5000)
