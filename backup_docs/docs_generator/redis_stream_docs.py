import redis
import os

OUTPUT_FILE = "docs/auto/redis_streams.md"

r = redis.Redis(host="localhost", port=6379)

def generate_docs():
    streams = r.keys("*")

    lines = []
    lines.append("# Redis Event Streams\n")
    lines.append("Automatically generated documentation of Redis streams.\n")

    for stream in streams:
        name = stream.decode()

        try:
            info = r.xinfo_stream(name)

            lines.append(f"## {name}")
            lines.append(f"Length: {info['length']}")
            lines.append("")
        except:
            continue

    os.makedirs("docs/auto", exist_ok=True)

    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    generate_docs()
