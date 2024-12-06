from flask_restful import Resource
from flask import request
from ..Modelos import db, Nota, NotaSchema

nota_schema = NotaSchema()

class VistaNota(Resource):
    def get(self):
        return[nota_schema.dump(Nota) for Nota in Nota.query.all()]
    
    def post(self):
        nueva_nota = Nota(
            id_actividad = request.json['id_actividad'],
            id_estudiante = request.json['id_estudiante'],
            calificacion = request.json['calificacion'],
            fecha_asignacion = request.json['fecha_asignacion']
        )
        db.session.add(nueva_nota)
        db.session.commit()
        return nota_schema.dump(nueva_nota), 201
    
s