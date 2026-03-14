import time

class ProcessMonitor:

    def monitor(self, services):

        while True:

            for name, service in services.items():

                process = service["process"]

                if process.poll() is not None:

                    print(f"{name} crashed")

                    if service["restart"]:

                        print(f"Restarting {name}")

                        new_process = service["manager"].start_service(
                            name,
                            service["config"]
                        )

                        service["process"] = new_process

            time.sleep(5)
