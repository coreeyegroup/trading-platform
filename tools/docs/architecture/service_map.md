# Service Architecture

```mermaid
graph TD

market_data_service --> candle_builder
candle_builder --> market_context_engine
market_context_engine --> strategy_engine
strategy_engine --> signal_validator
signal_validator --> policy_engine
policy_engine --> risk_engine
risk_engine --> execution_engine
execution_engine --> broker_adapter
broker_adapter --> trade_monitor
trade_monitor --> portfolio_engine
```
