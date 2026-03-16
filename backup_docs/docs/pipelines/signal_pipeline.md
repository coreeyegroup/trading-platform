# Signal Processing Pipeline

```mermaid
graph LR

market_ticks --> market_candles
market_candles --> validated_candles
validated_candles --> market_context

market_context --> strategy_inputs
strategy_inputs --> strategy_signals

strategy_signals --> validated_signals
validated_signals --> policy_approved_signals

policy_approved_signals --> risk_approved_orders
risk_approved_orders --> execution_orders

execution_orders --> execution_reports
execution_reports --> portfolio_updates
```
