import subprocess
import os

class ServiceManager:

    def start_service(self, service_name, config):

        service_path = config["path"]
        command = config["start_command"]

        full_path = os.path.expanduser(
            f"~/trading-platform/{service_path}"
        )

        print(f"Starting {service_name}...")

        process = subprocess.Popen(
            command,
            shell=True,
            cwd=full_path
        )

        return process
