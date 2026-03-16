# Automatic Architecture Diagram

Generated from running platform services.

```mermaid
graph TD
trading_redis[trading-redis]
trading_postgres[trading-postgres]
trading_grafana[trading-grafana]
trading_node_red[trading-node-red]
trading_prometheus[trading-prometheus]
market_context((market_context))
market_ticks((market_ticks))
validated_signals((validated_signals))
policy_approved_signals((policy_approved_signals))
strategy_inputs((strategy_inputs))
risk_approved_orders((risk_approved_orders))
validated_candles((validated_candles))
trade_signals((trade_signals))
strategy_signals((strategy_signals))
market_candles((market_candles))
test_stream((test_stream))
trading_redis --> trading_postgres
trading_postgres --> trading_grafana
trading_grafana --> trading_node_red
trading_node_red --> trading_prometheus
```