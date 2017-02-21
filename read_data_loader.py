import json
JSON_DATA_FILE = "read_data.json"
USER_DICT = dict()
PERMISSION_DICT = dict()
ROLE_DICT = dict()

class User(object):
    def __init__(self):
        self.id = None
        self.role_list = list()

class Role(object):
    def __init__(self):
        self.id = None

with open(JSON_DATA_FILE, 'r') as json_data:
    json_data_dict_init = json.loads(json_data.read())

    user_dict_list = json_data_dict_init.get("users")
    role_dict_list = json_data_dict_init.get("roles")
    permission_dict_list = json_data_dict_init.get("permissions")

    for permission_dict in permission_dict_list:
        PERMISSION_DICT[permission_dict['id']] = permission_dict['name']
    for role_dict in role_dict_list:
        ROLE_DICT[role_dict['id']] = role_dict['permissions']

    for user_dict in user_dict_list:
        USER_DICT[user_dict['id']]= user_dict['roles']