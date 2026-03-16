import redis
import subprocess
import os

OUTPUT_FILE = "docs/auto/architecture_diagram.md"


def get_docker_services():

    result = subprocess.run(
        ["docker", "ps", "--format", "{{.Names}}"],
        capture_output=True,
        text=True
    )

    return result.stdout.splitlines()


def get_redis_streams():

    try:
        r = redis.Redis(host="localhost", port=6379)
        streams = r.keys("*")
        return [s.decode() for s in streams]

    except:
        return []


def generate_diagram():

    services = get_docker_services()
    streams = get_redis_streams()

    lines = []

    lines.append("# Automatic Architecture Diagram\n")
    lines.append("Generated from running platform services.\n")

    lines.append("```mermaid")
    lines.append("graph TD")

    for s in services:
        node = s.replace("-", "_")
        lines.append(f"{node}[{s}]")

    if streams:
        for stream in streams:
            stream_node = stream.replace("-", "_")
            lines.append(f"{stream_node}(({stream}))")

    for i in range(len(services) - 1):
        a = services[i].replace("-", "_")
        b = services[i + 1].replace("-", "_")
        lines.append(f"{a} --> {b}")

    lines.append("```")

    os.makedirs("docs/auto", exist_ok=True)

    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    generate_diagram()
