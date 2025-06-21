#!/bin/bash

# Use environment variable or hardcoded token (less secure)
USERNAME="lavi324"
TOKEN="${GITHUB_PAT}"

# Set the remote URL using embedded PAT (only if not already set)
git remote set-url origin https://$USERNAME:$TOKEN@github.com/$USERNAME/sport-tables-ai.git

# Add, commit, and push
git add .
git commit -m "Initial commit"
git push origin main
