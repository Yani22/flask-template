from app.models.Manpower import Manpower
from app import db


class ManpowerService():

    def get_manpower(self):
        # NOTE: List comprehension
        mp = [{'project_id': manpower.project_id, 'manpower_name': manpower.manpower_name,
               'position': manpower.position, 'rate_per_hour': manpower.rate_per_hour} for manpower in
              Manpower.query.all()]
        return mp

    def add_manpower(self, project_id, manpower_name, position, rate_per_hour):
        equipments = Manpower(project_id=project_id, manpower_name=manpower_name, position=position,
                              rate_per_hour=rate_per_hour)
        db.session.add(equipments)
        db.session.commit()

        return

    def edit_manpower(self, manpower_id, data):
        # query
        ms = Manpower.query.filter_by(id=manpower_id)

        if ms.first():
            ms.update(data)
            db.session.commit()

        else:
            raise Exception('Project Not Found')

        return

    def delete_manpower(self, manpower_id):
        # query
        ms = Manpower.query.filter_by(id=manpower_id)

        if ms.first():
            ms.delete()
            db.session.commit()

        else:
            raise Exception('Project Not Found')

        return