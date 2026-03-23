import subprocess
import sys

def check_host_status(hostname: str) -> str:
    if not isinstance(hostname, str):
        raise TypeError("hostname must be a string")
    if not hostname:
        raise ValueError("hostname cannot be empty.")
    
    status = ""
    try:
        ping = subprocess.run(
            ["ping", "-c", "3", hostname],
            check=True,
            capture_output=True,
            text=True,
            timeout=5
        )
    except subprocess.CalledProcessError as err:
        print(f"Faced error due to : {err.stderr}")
        status = "offline"
    except subprocess.TimeoutExpired as err:
        print(f"Timeout expired...")
        status = "offline"
    else: 
        print(ping.stdout)
        status = "online"

    return status

if __name__ == "__main__":
    print(check_host_status("192.168.2.20"))