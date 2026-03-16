# Service Name

## Overview

Describe the purpose of the service.

---

## Responsibilities

- responsibility 1
- responsibility 2
- responsibility 3

---

## Inputs

| Source | Stream | Description |
|------|------|------|
| Service | stream_name | description |

---

## Outputs

| Destination | Stream | Description |
|------|------|------|
| Service | stream_name | description |

---

## Event Streams

List Redis streams used by the service.

example:

market_context  
strategy_inputs  
strategy_signals  

---

## Configuration

Configuration variables used by the service.

| Variable | Description |
|--------|--------|
| CONFIG_NAME | description |

---

## Dependencies

External services required.

- Redis
- PostgreSQL
- API Gateway

---

## Failure Modes

Possible failures and how the system handles them.

Example:

- Redis connection loss
- malformed event message
- broker API failure

---

## Operational Notes

Operational guidance for running the service.

Example:

Restart command:

