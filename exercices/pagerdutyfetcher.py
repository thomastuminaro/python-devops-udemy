import requests

def get_incident_summary(api_url: str, api_key: str, service_id: str):
    if not all(isinstance(arg, str) and arg for arg in [api_url, api_key, service_id]):
        raise ValueError
    api_url = f"{api_url.rstrip('/')}/incidents"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    params = {
        "service_ids[]": service_id,
        "statuses[]": "triggered"
    }

    try:
        res = requests.get(url=api_url, params=params, headers=headers)
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        return
    else:
        return [f"[{incident.get('urgency', '').upper()}] {incident.get('id', '')}: {incident.get('title', '')}" for incident in res.json().get("incidents", [])] #type: ignore
