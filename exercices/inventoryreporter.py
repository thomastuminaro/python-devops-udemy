def validate_server(server: dict) -> bool:
    if not isinstance(server, dict):
        return False
    elif [ key for key in server.keys() ] != ["name", "region", "status"] :
        return False
    elif server["name"] == "" or not isinstance(server["name"], str):
        return False
    elif server["region"] == "" or not isinstance(server["region"], str):
        return False
    elif not server["status"] in ["active", "inactive"]:
        return False 
    else:
        return True
    

def generate_inventory_report(servers: list[dict]) -> dict:
    report = {}
    validated = [server for server in servers if validate_server(server)]

    for server in validated:
        report[server["region"]] = {         
            'active': [ srv["name"] for srv in validated if srv["status"] == "active" and srv["region"] == server["region"] ],
            'inactive': [ srv["name"] for srv in validated if srv["status"] == "inactive" and srv["region"] == server["region"] ]
        }
 
    return report

if __name__ == "__main__":
    server_list = [
        {'name': 'web-01', 'region': 'us-east-1', 'status': 'active'},
        {'name': 'db-01', 'region': 'eu-west-1', 'status': 'active'},
        {'name': 'app-01', 'region': 'us-east-1', 'status': 'inactive'},
        {'name': 'web-02', 'region': 'us-east-1', 'status': 'active'},
        {'region': 'us-east-1', 'status': 'active'},
        {'name': 'monitor-01', 'region': 'eu-west-1', 'status': 'down'} # Invalid status
    ]

    print(generate_inventory_report(server_list))