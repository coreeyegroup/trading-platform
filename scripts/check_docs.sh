#!/bin/bash

changed_files=$(git diff --name-only HEAD~1)

if echo "$changed_files" | grep "services/" && ! echo "$changed_files" | grep "docs/services/"
then
  echo "ERROR: Service changed but documentation not updated."
  exit 1
fi
