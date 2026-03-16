# Risk Engine

## Overview

The Risk Engine validates trading orders against risk constraints.

---

## Responsibilities

- position size validation
- account exposure checks
- portfolio risk control

---

## Inputs

| Source | Stream | Description |
|------|------|------|
| policy_engine | policy_approved_signals | validated signals |

---

## Outputs

| Destination | Stream | Description |
|------|------|------|
| execution_engine | risk_approved_orders | approved orders |

---

## Event Streams

policy_approved_signals  
risk_approved_orders  

---

## Dependencies

- Redis Streams
- portfolio state database

---

## Failure Modes

- missing portfolio state
- invalid signal message
- database access failure
