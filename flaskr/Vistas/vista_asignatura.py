from flask_restful import Resource
from flask import request
from ..Modelos import db, Asignatura, AsignaturaSchema

asignatura_schema = AsignaturaSchema()

class VistaAsignatura(Resource):
    def get(self):
        return[asignatura_schema.dump(Asignatura) for Asignatura in Asignatura.query.all()]
    
    
    
    def post(self):
        nueva_asignatura = Asignatura(
            nombre_asignatura = request.json['nombre_asignatura'],
            id_curso = request.json['id_curso']
        )
        db.session.add(nueva_asignatura)
        db.session.commit()
        return asignatura_schema.dump(nueva_asignatura), 201
    
    def put(self, id):
        asignatura = Asignatura.query.get_or_404(id)
        asignatura.nombre_asignatura = request.json.get("nombre_asignatura", asignatura.nombre_asignatura)
        asignatura.id_curso = request.json.get("id_curso", asignatura.id_curso)
        db.session.commit()
        return asignatura_schema.dump(asignatura), 200
    
    def delete(self, id):
        asignatura = Asignatura.query.get_or_404(id)
        db.session.delete(asignatura)
        db.session.commit()
        return 'Asignatura eliminada exitosamente.', 204
