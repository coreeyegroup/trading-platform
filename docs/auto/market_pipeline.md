# Market Pipeline Visualization

Last updated: 2026-03-16 13:22:28.040069 UTC

## Pipeline Diagram

```mermaid
graph LR
market_ticks[market_ticks (13650)] --> market_candles[market_candles (2572)]
market_candles[market_candles (2572)] --> validated_candles[validated_candles (2502)]
validated_candles[validated_candles (2502)] --> market_context[market_context (2450)]
market_context[market_context (2450)] --> strategy_inputs[strategy_inputs (2)]
strategy_inputs[strategy_inputs (2)] --> strategy_signals[strategy_signals (10)]
strategy_signals[strategy_signals (10)] --> validated_signals[validated_signals (50)]
validated_signals[validated_signals (50)] --> policy_approved_signals[policy_approved_signals (250)]
policy_approved_signals[policy_approved_signals (250)] --> risk_approved_orders[risk_approved_orders (1000)]
risk_approved_orders[risk_approved_orders (1000)] --> execution_orders[execution_orders (0)]
execution_orders[execution_orders (0)] --> execution_reports[execution_reports (0)]
execution_reports[execution_reports (0)] --> portfolio_updates[portfolio_updates (0)]
```

## Stream Statistics

- market_ticks: 13650 events
- market_candles: 2572 events
- validated_candles: 2502 events
- market_context: 2450 events
- strategy_inputs: 2 events
- strategy_signals: 10 events
- validated_signals: 50 events
- policy_approved_signals: 250 events
- risk_approved_orders: 1000 events
- execution_orders: 0 events
- execution_reports: 0 events
- portfolio_updates: 0 events