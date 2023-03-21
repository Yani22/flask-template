from app.models.Equipment import Equipment
from app import db


class EquipmentService():

    def get_equipment(self):
        # NOTE: List comprehension
        equipments = [{'project_id': equipment.project_id, 'equipment_name': equipment.equipment_name,
                       'price': equipment.price, 'quantity': equipment.quantity} for equipment in Equipment.query.all()]
        return equipments

    def add_equipment(self, project_id, equipment_name, price, quantity):
        equipments = Equipment(project_id=project_id, equipment_name=equipment_name, price=price, quantity=quantity)
        db.session.add(equipments)
        db.session.commit()

        return

    def edit_equipment(self, equipment_id, data):
        # query
        equipments = Equipment.query.filter_by(id=equipment_id)

        if equipments.first():
            equipments.update(data)
            db.session.commit()

        else:
            raise Exception('Project Not Found')

        return

    def delete_equipment(self, equipment_id):
        # query
        equipments = Equipment.query.filter_by(id=equipment_id)

        if equipments.first():
            equipments.delete()
            db.session.commit()

        else:
            raise Exception('Project Not Found')

        return