import re
from typing import Optional

def parse_login_event(log_line: str) -> Optional[dict[str, str]]:
    if not isinstance(log_line, str):
        raise TypeError("log_line must be a string.")

    pattern = r"^LOGIN_EVENT:\s+User\s+'(?P<username>[A-Za-z]+)'\s+.*\s+(?P<status>[A-Z]+)\.$"
    m = re.match(pattern, log_line)
    if m:
        return m.groupdict()
    else: 
        return None
    
if __name__ == "__main__":
    log1 = "LOGIN_EVENT: User 'jdoe' login attempt was SUCCESSFUL."
    log2 = "LOGIN_EVENT: User 'admin' login attempt was FAILED."
    log3 = "INFO: Application started."
    log4 = "LOGIN_EVENT: User 'guest' logged out"

    print(parse_login_event(log1))  # Expected: {'username': 'jdoe', 'status': 'SUCCESSFUL'}
    print(parse_login_event(log2))  # Expected: {'username': 'admin', 'status': 'FAILED'}
    print(parse_login_event(log3))  # Expe
    print(parse_login_event(log4))