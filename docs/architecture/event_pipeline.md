# Event Pipeline

```mermaid
graph TD

market_ticks --> market_candles
market_candles --> validated_candles
validated_candles --> market_context
market_context --> strategy_inputs
strategy_inputs --> strategy_engine
strategy_engine --> strategy_signals
strategy_signals --> signal_validator
signal_validator --> policy_engine
policy_engine --> risk_engine
risk_engine --> execution_engine
execution_engine --> broker_adapter
broker_adapter --> execution_reports
execution_reports --> portfolio_updates
