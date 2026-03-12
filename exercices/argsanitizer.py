def sanitize_hostname(func):
    """
    A decorator that finds a 'hostname' keyword argument, sanitizes it
    (lowercase, stripped whitespace), and passes it to the wrapped function.
    """
    def wrapper(*args, **kwargs):
        try:
            kwargs["hostname"] = kwargs["hostname"].strip().lower()
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error : {e}")
    return wrapper

@sanitize_hostname
def connect_to_host(*args, hostname):
    """Establishes a connection to a host."""
    print(f"Connecting to sanitized hostname: '{hostname}'")
    return f"Connected to {hostname}"
 
if __name__ == "__main__":
    print(connect_to_host(1, 2, 3, hostname="  PROD-API.local  "))
    print(connect_to_host(hostname="hostname.local"))