import redis
from datetime import datetime

OUTPUT_FILE = "docs/auto/market_pipeline.md"

PIPELINE = [
    "market_ticks",
    "market_candles",
    "validated_candles",
    "market_context",
    "strategy_inputs",
    "strategy_signals",
    "validated_signals",
    "policy_approved_signals",
    "risk_approved_orders",
    "execution_orders",
    "execution_reports",
    "portfolio_updates",
]


def get_stream_length(stream):
    try:
        r = redis.Redis(host="localhost", port=6379)
        info = r.xinfo_stream(stream)
        return info["length"]
    except:
        return 0


def generate_pipeline():

    counts = {s: get_stream_length(s) for s in PIPELINE}

    lines = []

    lines.append("# Market Pipeline Visualization\n")
    lines.append(f"Last updated: {datetime.utcnow()} UTC\n")

    lines.append("## Pipeline Diagram\n")

    lines.append("```mermaid")
    lines.append("graph LR")

    for i in range(len(PIPELINE)-1):

        a = PIPELINE[i]
        b = PIPELINE[i+1]

        a_label = f"{a} ({counts[a]})"
        b_label = f"{b} ({counts[b]})"

        lines.append(f"{a.replace('-','_')}[{a_label}] --> {b.replace('-','_')}[{b_label}]")

    lines.append("```")

    lines.append("\n## Stream Statistics\n")

    for s in PIPELINE:
        lines.append(f"- {s}: {counts[s]} events")

    with open(OUTPUT_FILE,"w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    generate_pipeline()
