from app.services.ManpowerService import ManpowerService
from utils.format_response import format_response
from app.constants.status_codes import *
from app.constants.status_messages import *


class ManpowerController():

    @classmethod
    def get_manpower(cls):
        try:
            ms = ManpowerService()
            manpower = ms.get_manpower()
            return format_response(OK, OK_MESSAGE, manpower)
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))

    @classmethod
    def add_manpower(cls, project_id, manpower_name, position, rate_per_hour):
        try:
            ms = ManpowerService()
            ms.add_manpower(project_id, manpower_name, position, rate_per_hour)
            return format_response(OK, OK_MESSAGE, {})
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))

    @classmethod
    def edit_manpower(cls, manpower_id, data):
        try:
            ms = ManpowerService()
            ms.edit_manpower(manpower_id, data)
            return format_response(OK, OK_MESSAGE, {})
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))

    @classmethod
    def delete_manpower(cls, manpower_id):
        try:
            ms = ManpowerService()
            ms.delete_manpower(manpower_id)
            return format_response(OK, OK_MESSAGE, {})
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))