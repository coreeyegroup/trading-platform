#!/bin/bash

echo "Generating Redis stream documentation..."
python platform/docs_generator/redis_stream_docs.py

echo "Generating Docker services documentation..."
python platform/docs_generator/docker_architecture.py

echo "Generating database schema documentation..."
python platform/docs_generator/db_schema_docs.py

echo "Generating full architecture map..."
python platform/docs_generator/full_architecture_map.py

echo "Documentation generation complete."
