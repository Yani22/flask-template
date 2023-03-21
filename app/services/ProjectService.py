from app.models.Project import Project
from app import db

class ProjectService():
    
    def get_projects(self):
        # NOTE: List comprehension 
        projects = [{'id': project.id, 'name': project.name} for project in Project.query.all()]
        return projects
    
    def add_project(self, project_name, location):
        project = Project(name=project_name, location=location)
        db.session.add(project)
        db.session.commit()

        return
    
    def edit_project(self, project_id, data):
        # query
        project = Project.query.filter_by(id=project_id)

        if project.first():
            project.update(data)
            db.session.commit()

        else:
            raise Exception('Project Not Found')

        return 
    
    def delete_project(self, project_id):
        # query
        project = Project.query.filter_by(id=project_id)

        if project.first():
            project.delete()
            db.session.commit()

        else:
            raise Exception('Project Not Found')

        return