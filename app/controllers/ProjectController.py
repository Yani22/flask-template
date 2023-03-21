from app.services.ProjectService import ProjectService
from utils.format_response import format_response
from app.constants.status_codes import *
from app.constants.status_messages import *


class ProjectController():
    
    @classmethod
    def get_projects(cls):
        try:
            ps = ProjectService()
            projects = ps.get_projects()
            return format_response(OK, OK_MESSAGE, projects)
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))
    
    @classmethod
    def add_project(cls, project_name, location):
        try:
            ps = ProjectService()
            ps.add_project(project_name, location)
            return format_response(OK, OK_MESSAGE, {})
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))
    
    @classmethod
    def edit_project(cls, project_id, data):
        try:
            ps = ProjectService()
            ps.edit_project(project_id, data)
            return format_response(OK, OK_MESSAGE, {})
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))
    
    @classmethod
    def delete_project(cls, project_id):
        try:
            ps = ProjectService()
            ps.delete_project(project_id)
            return format_response(OK, OK_MESSAGE, {})
        except Exception as e:
            print(e)
            return format_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE, str(e))