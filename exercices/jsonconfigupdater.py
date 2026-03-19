import json
from pathlib import Path

def update_image_tag(config_path: str | Path, service_name: str, new_tag: str) -> None:
    if not isinstance(config_path, Path) and not isinstance(config_path, str):
        raise TypeError("config_path must be string or Path")
    
    configfile = config_path
    if isinstance(config_path, str):
        configfile = Path(config_path)

    if not configfile.exists(): #type: ignore
        raise FileNotFoundError(f"{configfile.name} does not exist.") #type: ignore
    
    if not isinstance(service_name, str) or not isinstance(new_tag, str):
        raise TypeError("service_name and new_tag must be string.") 
    if service_name == "" or new_tag == "":
        raise ValueError("service_name and new_tag must not be empty.")
    
    try:
        with configfile.open("r", encoding="utf-8") as file: #type: ignore
            data = json.load(file)

        data["services"][service_name]["image_tag"] = new_tag

        with configfile.open("w", encoding="utf-8") as file: #type: ignore
            json.dump(data, file, indent=4) #type: ignore

    except KeyError as err:
        raise err
    except Exception as err:
        raise err
    
if __name__ == "__main__":
    config_file = Path(__file__).parent / "files/config.json"
    update_image_tag(config_file, "api-gateway", "10.10.2")