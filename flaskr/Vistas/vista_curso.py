from flask_restful import Resource
from flask import request
from ..Modelos import db, Curso, CursoSchema

curso_schema = CursoSchema()

class VistaCurso(Resource):
    def get(self):
        return[curso_schema.dump(Curso) for Curso in Curso.query.all()]
    
    
    
    def post(self):
        nuevo_curso = Curso(
            nombre_curso = request.json['nombre_curso'],
            descripcion = request.json['descripcion']
        )
        db.session.add(nuevo_curso)
        db.session.commit()
        return curso_schema.dump(nuevo_curso), 201
    
    def put(self, id):
        curso = Curso.query.get_or_404(id)
        curso.nombre_curso = request.json.get('nombre_curso', curso.nombre_curso)
        curso.descripcion = request.json.get('descripcion', curso.descripcion)
        db.session.commit()
        return curso_schema.dump(curso)
    
    def delete(self, id):
        curso = Curso.query.get_or_404(id)
        db.session.delete(curso)
        db.session.commit()
        return 'Curso eliminado exitosamente.', 204
