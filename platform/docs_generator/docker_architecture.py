import subprocess

OUTPUT_FILE = "docs/auto/docker_services.md"

def get_containers():

    result = subprocess.run(
        ["docker", "ps", "--format", "{{.Names}}"],
        capture_output=True,
        text=True
    )

    return result.stdout.splitlines()


def generate_docs():

    containers = get_containers()

    lines = []
    lines.append("# Docker Services\n")
    lines.append("Automatically generated list of running platform services.\n")

    for c in containers:
        lines.append(f"- {c}")

    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    generate_docs()
