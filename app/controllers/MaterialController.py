from app.services.MaterialService import MaterialService
from utils.format_response import format_response
from app.constants.status_codes import *
from app.constants.status_messages import *


class MaterialController():

    @classmethod
    def get_materials(cls):
        try:
            ms = MaterialService()
            materials = ms.get_materials()
            return format_response(OK, OK_MESSAGE, materials)
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))

    @classmethod
    def add_material(cls, project_id, material_name, price, quantity):
        try:
            ms = MaterialService()
            ms.add_material(project_id, material_name, price, quantity)
            return format_response(OK, OK_MESSAGE, {})
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))

    @classmethod
    def edit_material(cls, material_id, data):
        try:
            ms = MaterialService()
            ms.edit_material(material_id, data)
            return format_response(OK, OK_MESSAGE, {})
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))



    @classmethod
    def delete_material(cls, material_id):
        try:
            ms = MaterialService()
            ms.delete_project(material_id)
            return format_response(OK, OK_MESSAGE, {})
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))