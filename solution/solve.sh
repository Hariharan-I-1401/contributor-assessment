#!/bin/bash
# Do NOT use set -e or set -euo pipefail

# 1. Configure a dummy Git identity (REQUIRED for merging inside a Docker container)
git config --global user.email "oracle@terminal-bench.com"
git config --global user.name "Oracle Agent"

# 2. Ensure we are firmly on the master branch
git checkout master

# 3. Merge the state the repo was in right before the previous checkout.
git merge -m "Recovering lost changes" -X theirs HEAD@{1}