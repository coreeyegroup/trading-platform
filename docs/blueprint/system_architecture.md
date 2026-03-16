# System Architecture

The trading platform is designed as a distributed event-driven system.

Core architecture layers:

1. UI Layer
2. API Gateway
3. Event Bus
4. Trading Engine Services
5. Storage Layer
6. Infrastructure Layer

## Architecture Overview

```mermaid
graph TD

UI --> API_Gateway
API_Gateway --> Event_Bus

Event_Bus --> Market_Data_Service
Event_Bus --> Strategy_Engine
Event_Bus --> Risk_Engine
Event_Bus --> Execution_Engine

Execution_Engine --> Broker_Adapter

Broker_Adapter --> Exchange
Exchange --> Execution_Reports
Execution_Reports --> Portfolio_Engine

This describes the **platform architecture layers** defined in your system design. :contentReference[oaicite:1]{index=1}
