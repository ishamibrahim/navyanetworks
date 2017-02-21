from flask import Flask
from flask_restful import Api
from views import HealthView, UserView, UserListView, PermissionCheckView, RoleView, PermissionView


app = Flask(__name__)
api = Api(app)
app.debug = True

@app.errorhandler(500)
def internal_error(exception):
    app.logger.exception(exception)
    return 'Internal Server Error', 500

@app.errorhandler(502)
def internal_error_502(exception):
    app.logger.exception(exception)
    return 'Internal Server Error', 500

@app.errorhandler(404)
def internal_error_502(exception):
    app.logger.exception(exception)
    return 'Page not found', 404


api.add_resource(HealthView, '/health')
api.add_resource(UserView, '/user/<string:user_id>')
api.add_resource(UserListView, '/user')
api.add_resource(PermissionCheckView, '/checkpermission/')
api.add_resource(RoleView, '/roles/<string:role_id>')
api.add_resource(PermissionView, '/permissions/<string:permission_id>')


if __name__ == '__main__':
    app.run()
