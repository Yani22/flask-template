from app.models.ProjectDetails import ProjectDetails
from app import db


class ProjectDetailsService():

    def get_project_details(self):
        # NOTE: List comprehension
        project_details = [{'project_id': project_detail.project_id, 'engineer': project_detail.engineer,
                            'architect': project_detail.architect, 'project_manager': project_detail.project_manager}
                           for project_detail in ProjectDetails.query.all()]
        return project_details

    def add_project_details(self, project_id, engineer, architect, project_manager):
        project_details = ProjectDetails(project_id=project_id, engineer=engineer, architect=architect,
                                         project_manager=project_manager)
        db.session.add(project_details)
        db.session.commit()

        return

    def edit_project_details(self, project_details_id, data):
        # query
        project_details = ProjectDetails.query.filter_by(id=project_details_id)

        if project_details.first():
            project_details.update(data)
            db.session.commit()

        else:
            raise Exception('Project Not Found')

        return

    def delete_project_details(self, project_details_id):
        # query
        project_details = ProjectDetails.query.filter_by(id=project_details_id)

        if project_details.first():
            project_details.delete()
            db.session.commit()

        else:
            raise Exception('Project Not Found')

        return