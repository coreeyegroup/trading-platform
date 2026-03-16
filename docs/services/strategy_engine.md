# Strategy Engine

## Overview

The Strategy Engine evaluates market context and generates trading signals.

---

## Responsibilities

- evaluate strategy conditions
- generate trade signals
- publish signals to event bus

---

## Inputs

| Source | Stream | Description |
|------|------|------|
| market_context_engine | market_context | processed market state |

---

## Outputs

| Destination | Stream | Description |
|------|------|------|
| signal_validator | strategy_signals | generated signals |

---

## Event Streams

strategy_inputs  
strategy_signals  

---

## Dependencies

- Redis Streams
- Strategy modules

---

## Failure Modes

- invalid strategy configuration
- missing market context
- message processing failure

---

## Operational Notes

The service must remain stateless and restartable.
