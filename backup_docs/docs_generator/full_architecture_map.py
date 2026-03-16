import subprocess
import redis
import os

OUTPUT_FILE = "docs/auto/full_architecture_map.md"


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


def generate_map():

    services = get_docker_services()
    streams = get_redis_streams()

    lines = []
    lines.append("# Full Trading Platform Architecture\n")
    lines.append("Automatically generated architecture map.\n")

    lines.append("```mermaid")
    lines.append("graph TD")

    lines.append("User[Trader]")
    lines.append("UI[Trading Dashboard]")
    lines.append("API[API Gateway]")
    lines.append("EventBus[(Redis Streams)]")
    lines.append("Database[(PostgreSQL)]")

    lines.append("User --> UI")
    lines.append("UI --> API")
    lines.append("API --> EventBus")

    for s in services:
        node = s.replace("-", "_")
        lines.append(f"{node}[{s}]")
        lines.append(f"EventBus --> {node}")

    for stream in streams:
        node = stream.replace("-", "_")
        lines.append(f"{node}(({stream}))")

    lines.append("Database --> PortfolioEngine")

    lines.append("```")

    os.makedirs("docs/auto", exist_ok=True)

    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    generate_map()
