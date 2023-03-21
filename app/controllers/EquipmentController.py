from app.services.EquipmentService import EquipmentService
from utils.format_response import format_response
from app.constants.status_codes import *
from app.constants.status_messages import *


class EquipmentController():

    @classmethod
    def get_equipment(cls):
        try:
            es = EquipmentService()
            equipment = es.get_equipment()
            return format_response(OK, OK_MESSAGE, equipment)
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))

    @classmethod
    def add_equipment(cls, project_id, equipment_name, price, quantity):
        try:
            es = EquipmentService()
            es.add_equipment(project_id, equipment_name, price, quantity)
            return format_response(OK, OK_MESSAGE, {})
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))

    @classmethod
    def edit_equipment(cls, equipment_id, data):
        try:
            es = EquipmentService()
            es.edit_equipment(equipment_id, data)
            return format_response(OK, OK_MESSAGE, {})
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))

    @classmethod
    def delete_equipment(cls, equipment_id):
        try:
            es = EquipmentService()
            es.delete_equipment(equipment_id)
            return format_response(OK, OK_MESSAGE, {})
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))