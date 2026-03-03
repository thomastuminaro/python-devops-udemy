required_packages = {"python", "pip", "pyside6", "pip", "kubernetes", "flask", "python", "ansible"}
print(required_packages)

print("ansible" in required_packages)
print("requests" in required_packages)

required_packages.add("paramiko")
print(required_packages)
required_packages.discard("pip")
print(required_packages)

installed = {"python", "kubernetes", "flask", "word"}

print(f"Missing requirements : {required_packages.difference(installed)}")
print(f"Extra packages : {installed.difference(required_packages)}")
print(f"Common packages : {required_packages.intersection(installed)}")