class Deployment:
    def __init__(self, service_name: str, environment: str):
        if not isinstance(service_name, str) and isinstance(environment, str):
            raise

        self.service_name = service_name
        self.environment = environment
        self.status = "pending"
        self.history = []

    def deploy(self, new_version: str):
        self.history.append(new_version)
        self.status = "deployed"

    def rollback(self) -> bool:
        if len(self.history) < 2:
            return False
        else:
            try:
                self.history.pop(-1)
            except Exception as e:
                return False
            else:
                self.status = "rolled_back"
                return True

    def check_status(self) -> dict:
        return {
            'service_name': self.service_name,
            'environment': self.environment,
            'status': self.status,
            'version': self.history[-1] if self.history else None
        }

if __name__ == "__main__":
    test = Deployment(service_name="mysvc", environment="prod")
    print(test.check_status())

    test.deploy(new_version="v1.0.0")
    print(test.check_status())

    test.deploy(new_version="v2.0.0")
    print(test.check_status())

    test.rollback()
    print(test.check_status())

    test.rollback()
    print(test.check_status())

    test.rollback()
    print(test.check_status())