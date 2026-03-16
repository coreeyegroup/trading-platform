# Execution Pipeline Design

The execution pipeline converts approved trading signals into broker orders.

## Pipeline

validated_signals  
→ policy_approved_signals  
→ risk_approved_orders  
→ execution_orders  
→ execution_reports
