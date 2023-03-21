from app.services.ProjectDetailsService import ProjectDetailsService
from utils.format_response import format_response
from app.constants.status_codes import *
from app.constants.status_messages import *


class ProjectDetailsController():

    @classmethod
    def get_project_details(cls):
        try:
            pds = ProjectDetailsService()
            project_details = pds.get_project_details()
            return format_response(OK, OK_MESSAGE, project_details)
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))

    @classmethod
    def add_project_details(cls, project_id, engineer, architect, project_manager):
        try:
            pds = ProjectDetailsService()
            pds.add_project_details(project_id, engineer, architect, project_manager)
            return format_response(OK, OK_MESSAGE, {})
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))

    @classmethod
    def edit_project_details(cls, project_details_id, data):
        try:
            pds = ProjectDetailsService()
            pds.edit_project_details(project_details_id, data)
            return format_response(OK, OK_MESSAGE, {})
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))

    @classmethod
    def delete_project_details(cls, project_details_id):
        try:
            pds = ProjectDetailsService()
            pds.delete_project_details(project_details_id)
            return format_response(OK, OK_MESSAGE, {})
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))