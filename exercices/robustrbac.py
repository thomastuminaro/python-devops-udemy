import functools

class AuthorizationError(Exception):
    def __init__(self, user_name, required_role):
        self.user_name = user_name
        self.required_role = required_role
        msg = f"User '{self.user_name}' lacks the required role: '{self.required_role}'."
        super().__init__(msg)

def require_role(required_role):
    """
    A decorator factory that creates a decorator to check for a specific user role, with robust validation and custom exceptions.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not "user" in kwargs.keys():
                raise ValueError("Cannot find user.")
            elif not isinstance(kwargs["user"], dict): 
                raise TypeError("Specified user isn't a dictionary.")
            elif "roles" not in kwargs["user"].keys() or not isinstance(kwargs["user"]["roles"], list):
                raise ValueError("Please check user definition and roles.")
            elif required_role not in kwargs["user"]["roles"]:
                raise AuthorizationError(user_name=kwargs["user"]["name"], required_role=required_role)
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator

@require_role('admin')
def restart_server(*, user, server_id):
    """Restarts a server after a permission check."""
    return f"Server {server_id} restart initiated by {user['name']}."

if __name__ == "__main__":
    admin_user = {'name': 'alice', 'roles': ['admin']}
    viewer_user = {'name': 'bob', 'roles': ['viewer']}
    malformed_user = ['name', 'eve']

    print(restart_server(user=admin_user, server_id='web-01'))
    print(restart_server(user=malformed_user, server_id='db-01'))