from flaskr import create_app
from .Modelos import db
from flask_restful import Api
from .Vistas import VistaActividad, VistaAsignatura, VistaCurso, VistaNota, VistaUsuario

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

api = Api(app)

api.add_resource(VistaActividad, '/actividades', '/actividades/<int:id>')
api.add_resource(VistaAsignatura, '/asignatura', '/asignatura/<int:id>')
api.add_resource(VistaCurso, '/curso', '/curso/<int:id>')
api.add_resource(VistaNota, '/nota', '/nota/<int:id>')
api.add_resource(VistaUsuario, '/usuario', '/usuario/<int:id>')