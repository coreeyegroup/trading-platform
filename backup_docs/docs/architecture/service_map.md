# Service Interaction Map

```mermaid
graph TD

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
```
