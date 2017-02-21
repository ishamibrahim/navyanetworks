from flask_restful import Resource, request
from flask import jsonify, abort
from read_data_loader import USER_DICT, ROLE_DICT, PERMISSION_DICT
from constants import *
from functools import wraps


class Auth:
    def __init__(self):
        pass

    def requires_auth(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            try:
                if not auth:
                    return self.no_authorisation_present()
                else:
                    if auth.username == SECRET_USER and auth.password == SECRET_KEY:
                        return f(*args, **kwargs)
                    else:
                        return self.invalid_credentials()
            except Exception:
                return self.invalid_credentials()

        return decorated

    def invalid_credentials(self):
        """ Sends a 401 response that enables basic auth"""
        resp = jsonify(message='Invalid credentials', error_code='invalid_credentials')
        resp.status_code = 401
        return resp

    def no_authorisation_present(self):
        resp = jsonify(message='Invalid authorization. Use an auth header',
                       error_code='invalid_auth_header')

        resp.status_code = 400
        return resp
auth = Auth()


class HealthView(Resource):
    def get(self):
        return jsonify({'Health': "So cool!"})


class UserView(Resource):
    @staticmethod
    def get_user_details(user_id):
        try:
            user_data_dict = USER_DICT.get(user_id)
            if user_data_dict:
                return user_data_dict, 200
            else:
                return DOESNT_EXIST_JSON, 404
        except Exception as e:
            return abort(404)

    @auth.requires_auth
    def get(self, user_id):
        status = UserView.get_user_details(user_id)
        return status


class UserListView(Resource):
    @auth.requires_auth
    def get(self):
        return jsonify(USER_DICT)


class PermissionCheckView(Resource):
    @auth.requires_auth
    def get(self):
        user_id = request.args['userid']
        permission_id = request.args['permissionid']

        user_roles_list = USER_DICT.get(user_id)
        if user_roles_list:
            for user_role in user_roles_list:
                if permission_id in ROLE_DICT[user_role]:
                    return {"status": True}, 200
        return {"status": False}, 200


class RoleView(Resource):
    @auth.requires_auth
    def get(self, role_id):
        permission_list = ROLE_DICT.get(role_id)
        if permission_list:
            return permission_list, 200
        else:
            return DOESNT_EXIST_JSON, 404

    @auth.requires_auth
    def post(self, role_id):
        json_data = request.get_json()
        if not json_data:
            abort(404)
        role_exists = ROLE_DICT.get(role_id)
        if role_exists:
            ROLE_DICT[role_id] = json_data['permissions']
            return SUCCESS_JSON, 201
        else:
            return DOESNT_EXIST_JSON, 404


class PermissionView(Resource):
    @auth.requires_auth
    def get(self, permission_id):
        permission_data = PERMISSION_DICT.get(permission_id)
        if permission_data:
            return {"permission": permission_data}, 200
        else:
            return DOESNT_EXIST_JSON, 404

    @auth.requires_auth
    def delete(self, permission_id):
        permission_exists = PERMISSION_DICT.get(permission_id)
        if permission_exists:
            PERMISSION_DICT.pop(permission_id)
            return SUCCESS_JSON, 204
        else:
            return DOESNT_EXIST_JSON, 404
