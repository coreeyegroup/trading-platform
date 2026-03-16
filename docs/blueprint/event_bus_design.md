# Event Bus Design

The platform uses Redis Streams for event communication.

## Responsibilities

- service communication
- asynchronous processing
- pipeline decoupling
- horizontal scalability

## Event Streams

market_ticks  
market_candles  
validated_candles  
market_context  
strategy_inputs  
strategy_signals  
validated_signals  
policy_approved_signals  
risk_approved_orders  
execution_orders  
execution_reports  
portfolio_updates
