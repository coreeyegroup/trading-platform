# Event Driven Architecture

The trading platform operates using event streams.

All services communicate via the event bus.

## Event Flow

```mermaid
graph TD

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
