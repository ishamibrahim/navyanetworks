# navyanetworks
Here are REST APIs to access and modify users, their roles and permissions.

<h2>Stack Details</h2>

`Python` + `Flask` + `FlaskRestful`

<h2>API Documentation</h2>
### END POINTS

- [GET /health](#get_health)
- [GET /user](#get_user)
- [GET /user/<:id>](#get_user_id)
- [GET /checkpermission](#check_permission)
- [GET /role/<:id>](#get_role_id)
- [POST /role/<:id>](#post_role_id)
- [GET /permissions/<:id>](#get_permission)
- [DELETE /permissions/<:id>](#del_permission)

---

### <a name="get_health"></a>GET /health
Checks if the server is available or not

*Success* - 
```json
{
  "Health": "So cool!"
}
```
---
### <a name="get_user"></a>GET /user
Returns a list of users registered in the network.

**Requires** - Authorization header. 

*Success* - returns a json of users and their roles
```json
{
  "user1": [
    "role1",
    "role3"
  ],
  "user2": [
    "role1"
  ]
}

```

---

### <a name="get_user_id"></a>GET /user/<:id>
Returns information about the specified user

**Requires** - Authorization header. 

*Success* - Returns rolesof a user
```json
[
    "role1",
    "role3"
]

```

---

### <a name="check_permission"></a>GET /checkpermission
Checks if the speicified user has the specified permission or not
Returns a boolean value.

**Requires** - Authorization header. 
form fields - 
- userid : The id of the user
- permissionid : The permission ID to match with the user.

*Success* - 
Returns a boolean status `true` if the user has the specified permission
```json
{
  "status": true
}
```
Returns a boolean status `false` if the user does not have the specified permission
```json
{
  "status": false
}
```

---

### <a name="get_role_id"></a>GET /role/<:id>
Gets the available permissions in the specified role

**Requires** - Authorization header. 

*Success* - 
Returns a list of permissions in the role
```json
[
  "perm1",
  "perm5"
]
```

---

### <a name="post_role_id"></a>POST /role/<:id>
Asigns the permissions sent to the specified role

**Requires** - Authorization header. 

-POST params

```json
{"permissions" : [
  "perm1", 
  "perm8"
]}
```

*Success* - Returns a list of permissions in the role

```json
{
  "message": "Success",
  "status": "success"
}
```

---

### <a name="get_permissions"></a>GET /permissions/<:id>
Gets the data about the specified permission

**Requires** - Authorization header.

*Success* - Returns a list of permissions in the role

```
{
  "permission": "Can withdraw"
}
```

---

### <a name="del_permission"></a>DELETE /permissions/<:id>
Delete the specified permission

**Requires** - Authorization header. 

-POST params

*Success* - 204
```
{}
```

*Failure* - 404
```json
{
  "message": "Does not exist",
  "status": "not_exist"
}
```

---

<h3> Static User Credentials </h3>
usename : `navya`
password : `dfd8cc06-74bb-43d9-9018-3a9d4513e932`

---

<h2> Set up </h2>
- git clone the __navyanetworks__ repo
- install pip
- install virtualenv or virtualenvwrapper
- `pip install -r requirements.txt`
- `export PYTHONPATH=<navyanetworks folder path>:$PYTHONPATH`
- `python runserver.py`


