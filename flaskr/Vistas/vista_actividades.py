from flask_restful import Resource
from flask import request
from ..Modelos import db, Actividad, ActividadSchema

actividad_schema = ActividadSchema()

class VistaActividad(Resource):
    def get(self):
        return [actividad_schema.dump(Actividad) for Actividad in Actividad.query.all()]
    
    def post(self):
        nueva_actividad = Actividad(
            nombre_actividad = request.json['nombre_actividad'],
            id_asignatura = request.json['id_asignatura'],
            porcentaje = request.json['porcentaje']
        )

        db.session.add(nueva_actividad)
        db.session.commit()
        return actividad_schema.dump(nueva_actividad), 201
    
    
    
    def put(self, id):
        actividad = Actividad.query.get_or_404(id)
        actividad.nombre_actividad = request.json.get("nombre_actividad", actividad.nombre_actividad)
        actividad.id_asignatura = request.json.get("id_asignatura", actividad.id_asignatura)
        actividad.porcentaje = request.json.get("porcentaje", actividad.porcentaje)
        db.session.commit()
        return actividad_schema.dump(actividad), 204
    
    def delete(self, id):
        actividad = Actividad.query.get_or_404(id)
        db.session.delete(actividad)
        db.session.commit()
        return 'Actividad Eliminada Correctamente', 204