from app.models.Material import Material
from app import db


class MaterialService():

    def get_materials(self):
        # NOTE: List comprehension
        materials = [{'project_id': material.project_id, 'material_name': material.material_name} for material in
                     Material.query.all()]
        return materials

    def add_material(self, project_id, material_name, price, quantity):
        material = Material(project_id=project_id, material_name=material_name, price=price, quantity=quantity)
        db.session.add(material)
        db.session.commit()

        return

    def edit_material(self, material_id, data):
        # query
        material = Material.query.filter_by(id=material_id)

        if material.first():
            material.update(data)
            db.session.commit()

        else:
            raise Exception('Project Not Found')

        return

    def delete_material(self, material_id):
        # query
        material = Material.query.filter_by(id=material_id)

        if material.first():
            material.delete()
            db.session.commit()

        else:
            raise Exception('Project Not Found')

        return