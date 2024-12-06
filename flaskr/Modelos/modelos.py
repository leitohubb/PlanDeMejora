from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    email = db.Column(db.String(50))
    contrasena = db.Column(db.String(50))
    rol = db.Column(db.String(50)) 
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'))  
    curso = db.relationship('Curso', back_populates='estudiantes', uselist=False)  
    notas = db.relationship('Nota', back_populates='estudiante_rl', uselist=False)  
class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_curso = db.Column(db.String(40))
    descripcion = db.Column(db.String(255))
    asignaturas = db.relationship('Asignatura', back_populates='curso_rl')
    estudiantes = db.relationship('Usuario', back_populates='curso', foreign_keys=[Usuario.curso_id])  

class Asignatura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_asignatura = db.Column(db.String(50))
    id_curso = db.Column(db.Integer, db.ForeignKey('curso.id'))
    curso_rl = db.relationship('Curso', back_populates='asignaturas')
    actividades = db.relationship('Actividad', back_populates='asignatura_rl')

class Actividad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_actividad = db.Column(db.String(50))
    id_asignatura = db.Column(db.Integer, db.ForeignKey('asignatura.id'))
    porcentaje = db.Column(db.Numeric(5,2))
    asignatura_rl = db.relationship('Asignatura', back_populates='actividades')
    notas = db.relationship('Nota', back_populates='actividad_rl')

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_actividad = db.Column(db.Integer, db.ForeignKey('actividad.id'))
    id_estudiante = db.Column(db.Integer, db.ForeignKey('usuario.id')) 
    calificacion = db.Column(db.Numeric(5,2))
    fecha_asignacion = db.Column(db.DateTime)
    actividad_rl = db.relationship('Actividad', back_populates='notas')
    estudiante_rl = db.relationship('Usuario', back_populates='notas')

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True

class CursoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Curso
        include_relationships = True
        load_instance = True

class AsignaturaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Asignatura
        include_relationships = True
        load_instance = True

class ActividadSchema(SQLAlchemyAutoSchema):
    asignatura_rl = fields.Nested(AsignaturaSchema)
    class Meta:
        model = Actividad
        include_relationships = True
        load_instance = True

class NotaSchema(SQLAlchemyAutoSchema):
    actividad_rl = fields.Nested(ActividadSchema)
    class Meta:
        model = Nota
        include_relationships = True
        load_instance = True
