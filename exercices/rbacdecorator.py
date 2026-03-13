from functools import wraps

def require_role(required_role):
    """Creates decorator to verify user permisssions

    Args:
        required_role (str): name of the role needed

    Returns:
        Role check decorator
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if [ role for role in kwargs["user"].get("roles", "") if role == required_role ]:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError(f"Current user does not have role {required_role}.")
            except Exception as e:
                raise
        return wrapper
    return decorator

@require_role('admin')
def restart_server(*, user, server_id):
    """Restarts a server after a permission check."""
    return f"Server {server_id} restart initiated by {user['name']}."

if __name__ == "__main__":
    admin_user = {'name': 'alice', 'roles': ['admin', 'viewer']}
    viewer_user = {'name': 'bob', 'roles': ['viewer']}

    print(restart_server.__doc__)
    print(restart_server(user=admin_user, server_id='web-01'))
    print(restart_server(user=viewer_user, server_id='db-01'))