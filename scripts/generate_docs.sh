#!/bin/bash

echo "Generating Redis stream documentation..."
python platform/docs_generator/redis_stream_docs.py

echo "Generating Docker services documentation..."
python platform/docs_generator/docker_architecture.py

echo "Generating database schema documentation..."
python platform/docs_generator/db_schema_docs.py

echo "Generating full architecture map..."
python platform/docs_generator/full_architecture_map.py

echo "Generating system status..."
python platform/docs_generator/system_status_docs.py

echo "Generating trading activity..."
python platform/docs_generator/trading_activity_docs.py

echo "Generating pipeline visualization..."
python platform/docs_generator/pipeline_visualization_docs.py

echo "Documentation generation complete."
