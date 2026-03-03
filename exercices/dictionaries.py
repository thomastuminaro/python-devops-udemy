server_info = {
    "id": "0001",
    "ip_address": "192.167.1.10",
    "state": "up",
    "tags" : {
        "Name": "my-host",
        "Project": "python-devops"
    }
}

print(server_info)
print(server_info.get("state"))

server_info["state"] = "stopped"
print(server_info.get("state"))

server_info["tags"].update({"AddedBy": "Code"})
print(server_info)

print(server_info.items())
for key, value in server_info.items():
    print(f"{key} : {value}")