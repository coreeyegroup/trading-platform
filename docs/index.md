# Trading Platform Documentation

Welcome to the documentation for the **Algorithmic Trading Platform**.

This platform is designed as a **distributed event-driven trading system** composed of multiple microservices communicating through an event bus.

---

# System Overview

```mermaid
graph TD

User[Trader]
UI[Trading Dashboard]
API[API Gateway]

EventBus[(Redis Event Bus)]

MarketData[Market Data Service]
CandleBuilder[Candle Builder]
MarketContext[Market Context Engine]

StrategyEngine[Strategy Engine]
SignalValidator[Signal Validator]

PolicyEngine[Policy Engine]
RiskEngine[Risk Engine]

ExecutionEngine[Execution Engine]
BrokerAdapter[Broker Adapter]

TradeMonitor[Trade Monitor]
PortfolioEngine[Portfolio Engine]

Database[(PostgreSQL)]

User --> UI
UI --> API
API --> EventBus

EventBus --> MarketData
MarketData --> CandleBuilder
CandleBuilder --> MarketContext

MarketContext --> StrategyEngine
StrategyEngine --> SignalValidator

SignalValidator --> PolicyEngine
PolicyEngine --> RiskEngine

RiskEngine --> ExecutionEngine
ExecutionEngine --> BrokerAdapter

BrokerAdapter --> TradeMonitor
TradeMonitor --> PortfolioEngine

PortfolioEngine --> Database
