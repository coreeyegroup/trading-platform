# Execution Engine

## Overview

The Execution Engine converts approved orders into broker API requests.

---

## Responsibilities

- send orders to broker
- track order execution
- publish execution reports

---

## Inputs

| Source | Stream | Description |
|------|------|------|
| risk_engine | risk_approved_orders | approved orders |

---

## Outputs

| Destination | Stream | Description |
|------|------|------|
| broker_adapter | execution_orders | broker order request |

---

## Event Streams

risk_approved_orders  
execution_orders  
execution_reports  

---

## Dependencies

- broker adapter
- Redis Streams

---

## Failure Modes

- broker API failure
- order rejection
- timeout during execution
