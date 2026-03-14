import yaml

from service_manager import ServiceManager
from process_monitor import ProcessMonitor


class PlatformSupervisor:

    def __init__(self):

        with open("service_registry.yaml") as f:
            self.config = yaml.safe_load(f)

        self.manager = ServiceManager()
        self.monitor = ProcessMonitor()

        self.services = {}

    def dependencies_satisfied(self, service_name, started):

        deps = self.config["services"][service_name].get("depends_on", [])

        for dep in deps:
            if dep not in started:
                return False

        return True

    def start_services(self):

        services = self.config["services"]

        started = set()

        while len(started) < len(services):

            for name, cfg in services.items():

                if name in started:
                    continue

                if self.dependencies_satisfied(name, started):

                    process = self.manager.start_service(name, cfg)

                    self.services[name] = {
                        "process": process,
                        "restart": cfg.get("restart", True),
                        "config": cfg,
                        "manager": self.manager
                    }

                    started.add(name)

                    print(f"Service started: {name}")

    def run(self):

        print("Starting trading platform services...")

        self.start_services()

        self.monitor.monitor(self.services)


if __name__ == "__main__":

    supervisor = PlatformSupervisor()

    supervisor.run()
