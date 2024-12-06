from flask_restful import Resource
from flask import request
from ..Modelos import db, Usuario, UsuarioSchema, Asignatura, Curso  # aqui elimina Profesor y Estudiante
from werkzeug.security import generate_password_hash

usuario_schema = UsuarioSchema()

class VistaUsuario(Resource):
    def get(self):
        return [usuario_schema.dump(Usuario) for Usuario in Usuario.query.all()]
    
    def post(self):
        rol = request.json.get('rol')
        if rol not in ['Estudiante', 'Profesor']:
            return {"message": "Rol no válido. Los roles válidos son 'Estudiante' o 'Profesor'."}, 400
        
        nuevo_usuario = Usuario(
            nombre=request.json['nombre'],
            apellido=request.json['apellido'],
            email=request.json['email'],
            contrasena=request.json['contrasena'],
            rol=request.json['rol']
        )
        
        
        db.session.add(nuevo_usuario)
        db.session.commit()

        return usuario_schema.dump(nuevo_usuario), 201
    
    def put(self, id):
        usuario = Usuario.query.get_or_404(id)
        usuario.nombre = request.json.get('nombre', usuario.nombre)
        usuario.apellido = request.json.get('apellido', usuario.apellido)
        usuario.email = request.json.get('email', usuario.email)
        usuario.contrasena = request.json.get('contrasena', usuario.contrasena)
        usuario.rol = request.json.get('rol', usuario.rol)

        db.session.commit()
        return usuario_schema.dump(usuario)
    
    def delete(self, id):
        usuario = Usuario.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return 'Se elimino el usuario exitosamente!.', 204 

def setup():
    db.create_all()
    if not Usuario.query.filter_by(email="leonardo@gmail.com").first():
        hashed_password = generate_password_hash("admin123", method='sha256')
        
        superadmin = Usuario(
            nombre="Leonardo",
            apellido="Castelblanco",
            email="leonardo@gmail.com",
            contraseña=hashed_password, 
            rol="Admin"
        )
        db.session.add(superadmin)
        db.session.commit()
    return usuario_schema.dump(superadmin)
