import requests
 
def trigger_jenkins_job(jenkins_url: str, job_name: str, auth_token: str) -> bool:
 
    if not all(isinstance(arg, str) and arg for arg in [jenkins_url, job_name, auth_token]):
        raise ValueError("All arguments must be non-empty strings.")
 
    url = f"{jenkins_url.rstrip('/')}/job/{job_name}/build"
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }
 
    try:
        response = requests.post(url, headers=headers)
    except requests.exceptions.RequestException:
        return False
 
    if response.status_code == 201:
        return True
    
    return False

if __name__ == "__main__":
    pass